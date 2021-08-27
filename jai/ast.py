from typing import List
from jai import Tokens


class AstFunctionCall:
    name: str = "function call"
    rule: List[Tokens] = [
        Tokens.Identifier,
        Tokens.LeftParen,
        Tokens.Identifier,
        Tokens.RightParen,
        Tokens.Semicolon,
    ]

    def __init__(
        self,
        funcname=0,
        leftparen=0,
        arg=0,
        rightparen=0,
        semicolon=0,
    ):
        self.funcname = funcname
        self.leftparen = leftparen
        self.arg = arg
        self.rightparen = rightparen
        self.semicolon = semicolon

        self.token = None

    def __repr__(self):
        return "AstFunctionCall(" + " ".join([str(a) for a in self.rule]) + ")"


class AstEmptyAssignment:
    name: str = "empty assignment"
    rule: List[Tokens] = [
        Tokens.Identifier,
        Tokens.Colon,
        Tokens.TypeName,
        Tokens.Semicolon,
    ]

    def __init__(
        self,
        identifier=0,
        colon=0,
        type_name=0,
        semicolon=0,
    ):
        self.identifier = identifier
        self.colon = colon
        self.type_name = type_name
        self.semicolon = semicolon

        self.token = None

    def __repr__(self):
        return "AstEmptyAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class AstIntAssignment:
    name: str = "int assignment"
    rule: List[Tokens] = [
        Tokens.Identifier,
        Tokens.Colon,
        Tokens.TypeName,
        Tokens.Assignment,
        Tokens.NumericLiteral,
        Tokens.Semicolon,
    ]

    def __init__(
        self,
        identifier=0,
        colon=0,
        type_name=0,
        assignment=0,
        numeric_literal=0,
        semicolon=0,
    ):
        self.identifier = identifier
        self.colon = colon
        self.type_name = type_name
        self.assignment = assignment
        self.numeric_literal = numeric_literal
        self.semicolon = semicolon

        self.token = None

    def __repr__(self):
        return "AstIntAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class AstStrAssignment:
    name: str = "str assignment"
    rule: List[Tokens] = [
        Tokens.Identifier,
        Tokens.Colon,
        Tokens.TypeName,
        Tokens.Assignment,
        Tokens.StringLiteral,
        Tokens.Semicolon,
    ]

    def __init__(
        self,
        identifier=0,
        colon=0,
        type_name=0,
        assignment=0,
        string_literal=0,
        semicolon=0,
    ):
        self.identifier = identifier
        self.colon = colon
        self.type_name = type_name
        self.assignment = assignment
        self.string_literal = string_literal
        self.semicolon = semicolon

        self.token = None

    def __repr__(self):
        return "AstStrAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


RULES = [AstEmptyAssignment, AstIntAssignment, AstStrAssignment, AstFunctionCall]
