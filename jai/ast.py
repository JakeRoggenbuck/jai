from typing import List
from jai import Tokens


class AstEmptyAssignment:
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

        self.name: str = "empty assignment"
        self.rule: List[Tokens] = [
            Tokens.Identifier,
            Tokens.Colon,
            Tokens.TypeName,
            Tokens.Semicolon,
        ]

        self.token = None

    def __repr__(self):
        return "AstEmptyAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class AstIntAssignment:
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

        self.name: str = "int assignment"
        self.rule: List[Tokens] = [
            Tokens.Identifier,
            Tokens.Colon,
            Tokens.TypeName,
            Tokens.Assignment,
            Tokens.NumericLiteral,
            Tokens.Semicolon,
        ]

        self.token = None

    def __repr__(self):
        return "AstIntAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class AstStrAssignment:
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

        self.name: str = "str assignment"
        self.rule: List[Tokens] = [
            Tokens.Identifier,
            Tokens.Colon,
            Tokens.TypeName,
            Tokens.Assignment,
            Tokens.StringLiteral,
            Tokens.Semicolon,
        ]

        self.token = None

    def __repr__(self):
        return "AstStrAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


RULES = [AstEmptyAssignment, AstIntAssignment, AstStrAssignment]
