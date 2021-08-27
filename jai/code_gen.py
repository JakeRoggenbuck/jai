from jai.ast import (
    AstIntAssignment,
    AstStrAssignment,
    AstEmptyAssignment,
    AstFunctionCall,
)

from jai.logger import log, Severity
from jai import Tokens


def int_assignment(node: AstIntAssignment):
    return f"int {node.identifier.part} = {node.numeric_literal.part};\n"


def str_assignment(node: AstStrAssignment):
    return f'string {node.identifier.part} = "{node.string_literal.part}";\n'


def empty_assignment(node: AstEmptyAssignment):
    if node.type_name.part == "str":
        type_name_string = "string"
    elif node.type_name.part == "int":
        type_name_string = "int"
    else:
        type_name_string = "void"
        log(f"Type `{node.type_name.part}` not understood", Severity.Error)

    return f"{type_name_string} {node.identifier.part};\n"


def func_call(node: AstFunctionCall):
    return f"{node.funcname.part}({node.arg.part});\n"


def gen(node):
    if isinstance(node, AstIntAssignment):
        return int_assignment(node)

    if isinstance(node, AstStrAssignment):
        return str_assignment(node)

    if isinstance(node, AstEmptyAssignment):
        return empty_assignment(node)

    if isinstance(node, AstFunctionCall):
        return func_call(node)
