from enum import Enum
from jai import Lexer, Token, Settings, EMPTY_TOKEN, Tokens
from jai.logger import Severity, log
from typing import List
from os.path import exists
from jai.mode import Mode
from jai.ast import ASTStmt
from more_itertools import locate
from dataclasses import dataclass


class DocType:
    NoType = 0
    Takes = 1
    Returns = 2


class FunctionDoc:
    def __init__(self, part, doctype, types):
        self.part: str = part
        self.doctype: DocType = doctype
        self.types: List[Token] = types


def interpret_function_doc(doc: str) -> FunctionDoc:
    """Interpret the comment on top of a function

    'takes' and 'returns' are keyword that can be in comments in top of a
    function. This functions job is to determine what doc type it is, and what
    types it includes. For example, 'takes int' would have doc type
    DocType.Takes and would return an int so
    Token('int', Tokens.TypeName.value)
    """
    # The stack of all the tokens, Identifier, TypeName, and Comma
    local_stack: Token = []
    # The stack for just TypeNames
    type_stack: Token = []

    # lex the documentation for the function
    current_token = EMPTY_TOKEN
    lexer = Lexer(doc, Settings.PARSE_STRING)
    # Get all the tokens in the function doc
    while current_token.token != Lexer.EOF:
        current_token = lexer.next()
        # Add all the tokens to local_stack
        local_stack.append(current_token)

    # Check that the documentation isn't empty
    if len(local_stack) < 1:
        log("Nothing in function doc", Severity.Error)

    doctype = DocType.NoType
    # Check what action the documentation is
    action = local_stack[0]
    if action.token == Tokens.Identifier.value:

        if action.part == "takes":
            doctype = DocType.Takes
        elif action.part == "returns":
            doctype = DocType.Returns
        else:
            # Will return doctype of default DocType.NoType
            log("Function doc has no type", Severity.Error)

        # For takes and return check for the pattern of a type name
        # followed by a comma unless it's the last one
        if doctype == DocType.Returns or doctype == DocType.Takes:
            for token in local_stack:
                if token.token == Tokens.TypeName:
                    type_stack.append(token)

    return FunctionDoc(doc, doctype, type_stack)


class EmptyAssignment:
    def __init__(
        self,
        type_name=NotImplemented,
        identifier=NotImplemented,
        semicolon=NotImplemented,
    ):
        self.type_name = type_name
        self.identifier = identifier
        self.semicolon = semicolon

        self.name: str = "empty assignment"
        self.rule: List[Tokens] = [Tokens.TypeName, Tokens.Identifier, Tokens.Semicolon]

    def filled(self):
        return (
            self.type_name is not NotImplemented
            and self.identifier is not NotImplemented
            and self.semicolon is not NotImplemented
        )

    def __repr__(self):
        return "EmptyAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


RULES = [EmptyAssignment]


def check_rules(statements):
    for rule_object in RULES:
        rule_object_instance = rule_object()

        name = rule_object_instance.name
        rule = rule_object_instance.rule

        # Find all places this rule can start
        locations = list(locate(statements, lambda x: x.token == rule[0].value))

        for location in locations:
            # each place a rule can occur

            current_count = 0
            for i, part in enumerate(rule):

                # Check bounds
                if (location + i) < len(statements):

                    # Check if the current token is where it should in accordance
                    # with the rule and it's location
                    if statements[location + i].token == part.value:
                        current_count += 1

            if current_count == len(rule):
                # The rule was followed

                new = [rule_object(*statements[location : location + len(rule)])]
                before = statements[0:location]
                after = statements[location + len(rule) :]

                statements = before + new + after

        log(str(statements), Severity.Error)


class Parser:
    def __init__(self, mode: Mode):
        self.statements = []
        self.mode = mode

        if mode == Mode.Interactive:
            self.error_severity = Severity.Error
        else:
            self.error_severity = Severity.Fatal

    def spawn_lexer(self, source: str):
        return Lexer(source, Settings.PARSE_STRING)

    def loop(self, source: str):
        lexer = self.spawn_lexer(source)

        current_token = EMPTY_TOKEN

        while current_token.token != Lexer.EOF:
            current_token = lexer.next()
            self.statements.append(current_token)
            check_rules(self.statements)

    def parse_source_file(self, filename: str):
        """Parser for a file"""
        if not exists(filename):
            log("File does not exist", Severity.Fatal)

        with open(filename, "r") as file:
            self.loop(file.read())

    def parse_line(self, line: str):
        """Parser for a single line"""
        if line != "":
            self.loop(line)
