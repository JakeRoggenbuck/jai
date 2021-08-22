from typing import List
from jai import Tokens


class EmptyAssignment:
    def __init__(
        self,
        type_name=0,
        identifier=0,
        semicolon=0,
    ):
        self.type_name = type_name
        self.identifier = identifier
        self.semicolon = semicolon

        self.name: str = "empty assignment"
        self.rule: List[Tokens] = [Tokens.TypeName, Tokens.Identifier, Tokens.Semicolon]

        self.token = None

    def __repr__(self):
        return "EmptyAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class IntAssignment:
    def __init__(
        self,
        type_name=0,
        identifier=0,
        assignment=0,
        numeric_literal=0,
        semicolon=0,
    ):
        self.type_name = type_name
        self.identifier = identifier
        self.assignment = assignment
        self.numeric_literal = numeric_literal
        self.semicolon = semicolon

        self.name: str = "int assignment"
        self.rule: List[Tokens] = [
            Tokens.TypeName,
            Tokens.Identifier,
            Tokens.Assignment,
            Tokens.NumericLiteral,
            Tokens.Semicolon,
        ]

        self.token = None

    def __repr__(self):
        return "IntAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


class StrAssignment:
    def __init__(
        self,
        type_name=0,
        identifier=0,
        assignment=0,
        string_literal=0,
        semicolon=0,
    ):
        self.type_name = type_name
        self.identifier = identifier
        self.assignment = assignment
        self.string_literal = string_literal
        self.semicolon = semicolon

        self.name: str = "str assignment"
        self.rule: List[Tokens] = [
            Tokens.TypeName,
            Tokens.Identifier,
            Tokens.Assignment,
            Tokens.StringLiteral,
            Tokens.Semicolon,
        ]

        self.token = None

    def __repr__(self):
        return "StrAssignment(" + " ".join([str(a) for a in self.rule]) + ")"


RULES = [EmptyAssignment, IntAssignment, StrAssignment]
