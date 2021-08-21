from enum import Enum
from jai import Lexer, Token, Settings, EMPTY_TOKEN, Tokens
from jai.logger import Severity, log


class DocType:
    NoType = 0
    Takes = 1
    Returns = 2


class FunctionDoc:
    def __init__(self, part, doctype, types):
        self.part = part
        self.doctype = doctype
        self.types = types


def interpret_function_doc(doc: str) -> FunctionDoc:
    local_stack = []
    type_stack = []
    # lex the documentation for the function
    current_token = EMPTY_TOKEN
    lexer = Lexer(doc, Settings.PARSE_STRING)
    while current_token.token != Lexer.EOF:
        current_token = lexer.next()
        local_stack.append(current_token)

    # Check that the documentation isn't empty
    if len(local_stack) < 1:
        log("Nothing in function doc", Severity.Error)

    doctype = DocType.NoType
    # Check what action the documentation is
    action = local_stack[0]
    print(action)
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
