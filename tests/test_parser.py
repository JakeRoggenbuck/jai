import unittest
from jai.parser import FunctionDoc, DocType, interpret_function_doc


class TestInterpretFunctionDoc(unittest.TestCase):
    def test_interpret_function_doc(self):
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
            self.assertTrue(func_doc.doctype == test["out"].doctype)


if __name__ == "__main__":
    unittest.main()
