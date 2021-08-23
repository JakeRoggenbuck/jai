from jai import Lexer, Token, Settings, EMPTY_TOKEN
from jai.jargs import get_args
from os.path import exists
from jai.logger import Severity, log
from jai.console import run_interactive
from jai.mode import Mode
from jai.parser import Parser

"""jai includes things for use in the parser along with being a lexer

- Enum called Tokens with each token
- Class called Token that has a part and a token attribute
    part being a string that is the original text
    token being the number that corresponds to the enum
- A few functions for help with lexing
- Settings is a bitfield for configuring the lexer
"""


def main():
    mode, filename, options, args = get_args()

    parser = Parser(mode, options)

    if mode == Mode.Filemode:
        parser.parse_source_file(filename)

    elif mode == Mode.Interactive:
        for line in run_interactive():
            parser.parse_line(line)


if __name__ == "__main__":
    main()
