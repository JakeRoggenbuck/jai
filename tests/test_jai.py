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
