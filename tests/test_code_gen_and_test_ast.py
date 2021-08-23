from jai import Token, Tokens
from jai.code_gen import int_assignment, str_assignment, empty_assignment
from jai.ast import AstIntAssignment, AstStrAssignment, AstEmptyAssignment


INT_CASES = [
    {
        "in": [
            Token("a", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("int", Tokens.TypeName.value),
            Token("=", Tokens.Assignment.value),
            Token("15", Tokens.NumericLiteral.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "int a = 15;\n",
    },
    {
        "in": [
            Token("b", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("int", Tokens.TypeName.value),
            Token("=", Tokens.Assignment.value),
            Token("20", Tokens.NumericLiteral.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "int b = 20;\n",
    },
]

STR_CASES = [
    {
        "in": [
            Token("a", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("str", Tokens.TypeName.value),
            Token("=", Tokens.Assignment.value),
            Token("jake", Tokens.NumericLiteral.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": 'string a = "jake";\n',
    },
    {
        "in": [
            Token("b", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("str", Tokens.TypeName.value),
            Token("=", Tokens.Assignment.value),
            Token("woo", Tokens.NumericLiteral.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": 'string b = "woo";\n',
    },
]

EMPTY_CASES = [
    {
        "in": [
            Token("a", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("str", Tokens.TypeName.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "string a;\n",
    },
    {
        "in": [
            Token("b", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("str", Tokens.TypeName.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "string b;\n",
    },
    {
        "in": [
            Token("a", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("int", Tokens.TypeName.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "int a;\n",
    },
    {
        "in": [
            Token("b", Tokens.Identifier.value),
            Token(":", Tokens.Colon.value),
            Token("int", Tokens.TypeName.value),
            Token(";", Tokens.Semicolon.value),
        ],
        "code_gen": "int b;\n",
    },
]


def test_AstIntAssignment():
    for case in INT_CASES:
        int_ast = AstIntAssignment(*case["in"])
        assert int_ast.rule == AstIntAssignment.rule
        assert int_ast.assignment.part == "="
        assert int_ast.identifier.part == case["in"][0].part


def test_int_assignment():
    for case in INT_CASES:
        int_ast = AstIntAssignment(*case["in"])
        out = int_assignment(int_ast)
        assert out == case["code_gen"]


def test_AstStrAssignment():
    for case in STR_CASES:
        str_ast = AstStrAssignment(*case["in"])
        assert str_ast.rule == AstStrAssignment.rule
        assert str_ast.assignment.part == "="
        assert str_ast.identifier.part == case["in"][0].part


def test_str_assignment():
    for case in STR_CASES:
        str_ast = AstStrAssignment(*case["in"])
        out = str_assignment(str_ast)
        assert out == case["code_gen"]


def test_AstEmptyAssignment():
    for case in EMPTY_CASES:
        empty_ast = AstEmptyAssignment(*case["in"])
        assert empty_ast.rule == AstEmptyAssignment.rule
        assert empty_ast.identifier.part == case["in"][0].part


def test_empty_assignment():
    for case in EMPTY_CASES:
        empty_ast = AstEmptyAssignment(*case["in"])
        out = empty_assignment(empty_ast)
        assert out == case["code_gen"]
