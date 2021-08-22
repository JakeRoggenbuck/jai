import jai


def test_is_char_symbol():
    cases = ["[", "]", "{", "}", "(", ")", ".", ",", ":", ";", "=", "'", '"', "\\"]
    for case in cases:
        assert jai.is_char_symbol(case)

    noncases = ["m", "!", "A", "a", "1", "4", "+"]
    for noncase in noncases:
        assert not jai.is_char_symbol(noncase)


def test_is_char_operator():
    cases = ["+", "-", "*", "/", "^", ">", "<"]
    for case in cases:
        assert jai.is_char_operator(case)

    noncases = [".", "m", "!", "A", "a", "1", "4"]
    for noncase in noncases:
        assert not jai.is_char_operator(noncase)


def test_is_char_whitespace():
    cases = [" ", "\n", "\t"]
    for case in cases:
        assert jai.is_char_whitespace(case)

    noncases = [".", "m", "!", "A", "a", "1", "4", "+"]
    for noncase in noncases:
        assert not jai.is_char_whitespace(noncase)


def test_is_char_numeric():
    cases = ["2", "3", "4", "9"]
    for case in cases:
        assert jai.is_char_numeric(case)

    noncases = [".", "m", "!", "A"]
    for noncase in noncases:
        assert not jai.is_char_numeric(noncase)


def test_is_single_quote():
    assert jai.is_single_quote("'")

    noncases = [".", "m", "!", "A"]
    for noncase in noncases:
        assert not jai.is_single_quote(noncase)


def test_is_double_quote():
    assert jai.is_double_quote('"')

    noncases = [".", "m", "!", "A"]
    for noncase in noncases:
        assert not jai.is_double_quote(noncase)


def test_ends_token():
    cases = [("a", " "), ("a", "\n"), ("+", "a"), ("]", "a")]
    for case in cases:
        assert jai.ends_token(*case)

    cases = [("a", "a"), ("a", "b"), ("a", "c"), ("a", "j")]
    for case in cases:
        assert not jai.ends_token(*case)


def test_is_part_numeric():
    cases = ["344", "4535", "3424.3432"]
    for case in cases:
        assert jai.is_part_numeric(case)

    noncases = ["a", "fsdf", "+++", "!"]
    for noncase in noncases:
        assert not jai.is_part_numeric(noncase)


class TestLexer:
    cases_parse_string = [
        {
            "in": "int a = 23;",
            "out": [
                jai.Token("int", jai.Tokens.TypeName.value),
                jai.Token("a", jai.Tokens.Identifier.value),
                jai.Token("=", jai.Tokens.Assignment.value),
                jai.Token("23", jai.Tokens.NumericLiteral.value),
                jai.Token(";", jai.Tokens.Semicolon.value),
                jai.Token("", jai.Tokens.EOF.value),
            ],
        },
        {
            "in": "str name = 'jake';",
            "out": [
                jai.Token("str", jai.Tokens.TypeName.value),
                jai.Token("name", jai.Tokens.Identifier.value),
                jai.Token("=", jai.Tokens.Assignment.value),
                jai.Token("jake", jai.Tokens.StringLiteral.value),
                jai.Token(";", jai.Tokens.Semicolon.value),
                jai.Token("", jai.Tokens.EOF.value),
            ],
        },
        {
            "in": '"hey";',
            "out": [
                jai.Token("hey", jai.Tokens.StringLiteral.value),
                jai.Token(";", jai.Tokens.Semicolon.value),
                jai.Token("", jai.Tokens.EOF.value),
            ],
        },
    ]

    cases_dont_parse_string = [
        {
            "in": 'str name = "jake";',
            "out": [
                jai.Token("str", jai.Tokens.TypeName.value),
                jai.Token("name", jai.Tokens.Identifier.value),
                jai.Token("=", jai.Tokens.Assignment.value),
                jai.Token('"', jai.Tokens.DoubleQuote.value),
                jai.Token("jake", jai.Tokens.Identifier.value),
                jai.Token('"', jai.Tokens.DoubleQuote.value),
                jai.Token(";", jai.Tokens.Semicolon.value),
                jai.Token("", jai.Tokens.EOF.value),
            ],
        }
    ]

    def test_lexer_parse_string(self):
        for case in TestLexer.cases_parse_string:
            lexer = jai.Lexer(case["in"], jai.Settings.PARSE_STRING)

            tokens = []
            current_token = jai.EMPTY_TOKEN

            while current_token.token != jai.Lexer.EOF:
                current_token = lexer.next()
                tokens.append(current_token)

            for found_token, out_token in zip(tokens, case["out"]):
                assert found_token.part == out_token.part
                assert found_token.token == out_token.token

    def test_lexer_dont_parse_string(self):
        for case in TestLexer.cases_dont_parse_string:
            lexer = jai.Lexer(case["in"], jai.Settings.NONE)

            tokens = []
            current_token = jai.EMPTY_TOKEN

            while current_token.token != jai.Lexer.EOF:
                current_token = lexer.next()
                tokens.append(current_token)

            for found_token, out_token in zip(tokens, case["out"]):
                assert found_token.part == out_token.part
                assert found_token.token == out_token.token
