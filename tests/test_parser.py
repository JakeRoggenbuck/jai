from jai.parser import FunctionDoc, DocType, interpret_function_doc
from jai import Token, Tokens


def test_interpret_function_doc():
    tests = [
        {
            "in": "takes int",
            "out": FunctionDoc(
                "takes int", DocType.Takes, [Token("int", Tokens.TypeName.value)]
            ),
        },
        {
            "in": "takes int, str",
            "out": FunctionDoc(
                "takes int, str",
                DocType.Takes,
                [
                    Token("int", Tokens.TypeName.value),
                    Token("str", Tokens.TypeName.value),
                ],
            ),
        },
        {
            "in": "returns int",
            "out": FunctionDoc(
                "returns int", DocType.Returns, [Token("int", Tokens.TypeName.value)]
            ),
        },
        {
            "in": "returns int, str",
            "out": FunctionDoc(
                "returns int, str",
                DocType.Returns,
                [
                    Token("int", Tokens.TypeName.value),
                    Token("str", Tokens.TypeName.value),
                ],
            ),
        },
    ]

    for test in tests:
        func_doc = interpret_function_doc(test["in"])
        assert func_doc.doctype == test["out"].doctype
        assert func_doc.part == test["out"].part

        for test_type, ret_type in zip(func_doc.types, test["out"].types):

            assert test_type.part == ret_type.part
            assert test_type.token == ret_type.token
