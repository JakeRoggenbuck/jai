from jai.parser import FunctionDoc, DocType, interpret_function_doc


def test_interpret_function_doc():
    tests = [
        {
            "in": "takes int",
            "out": FunctionDoc("takes int", DocType.Takes, ["int"]),
        },
        {
            "in": "takes int, str",
            "out": FunctionDoc("takes int, str", DocType.Takes, ["int", "str"]),
        },
        {
            "in": "returns int",
            "out": FunctionDoc("returns int", DocType.Returns, ["int"]),
        },
        {
            "in": "returns int, str",
            "out": FunctionDoc("returns int", DocType.Takes, ["int"]),
        },
    ]

    for test in tests:
        func_doc = interpret_function_doc(test["in"])
        assert func_doc.doctype == test["out"].doctype
