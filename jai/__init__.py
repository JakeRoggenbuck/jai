from .jai import (
    Token,
    Lexer,
    is_char_symbol,
    is_char_operator,
    is_char_whitespace,
    is_char_numeric,
    is_single_quote,
    is_double_quote,
    ends_token,
    is_part_numeric,
    token_num_to_name,
)
from enum import Enum


class Tokens(Enum):
    EOF = 0

    Function = 1
    Class = 2
    Struct = 3
    TypeName = 4
    Operator = 5

    LeftBrace = 6
    RightBrace = 7
    LeftBracket = 8
    RightBracket = 9
    LeftParen = 10
    RightParen = 11

    Dot = 12
    Comma = 13

    Assignment = 14
    Semicolon = 15
    Colon = 16
    Tag = 17
    Reference = 18
    Question = 19
    At = 20
    Percent = 21
    Bang = 22
    Til = 23
    BackSlash = 24

    Arrow = 25
    Equal = 26

    Space = 27
    Tab = 28
    Newline = 29

    SingleQuote = 30
    DoubleQuote = 31
    Identifier = 32
    NumericLiteral = 33
    StringLiteral = 34

    LoopExit = 35
    Return = 36

    Empty = 0xF09F


EOF_TOKEN = Token("", 0)
EMPTY_TOKEN = Token("", 0xF09F)


class Settings:
    PARSE_STRING = 0x1
    PARSE_COMMENTS = 0x10
    ALL = PARSE_STRING + PARSE_COMMENTS


__version__ = "0.1.1"
__author__ = "jakeroggenbuck & adamhutchings"
