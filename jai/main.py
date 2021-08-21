from jai import Lexer, Token, Settings, EMPTY_TOKEN
from jai.jargs import get_args
from os.path import exists
from jai.logger import Severity, log
from jai.console import run_interactive
from jai.mode import Mode

"""jai includes things for use in the parser along with being a lexer

- Enum called Tokens with each token
- Class called Token that has a part and a token attribute
    part being a string that is the original text
    token being the number that corresponds to the enum
- A few functions for help with lexing
- Settings is a bitfield for configuring the lexer
"""


def parser(filename: str):
    """Initial parser example"""
    current_token = EMPTY_TOKEN
    with open(filename, "r") as file:

        lexer = Lexer(file.read(), Settings.PARSE_STRING)

        while current_token.token != Lexer.EOF:
            current_token = lexer.next()

            print(current_token)


def main():
    mode, filename, options, args = get_args()

    if mode == Mode.Filemode:
        if not exists(filename):
            log("File does not exist", Severity.Fatal)

        parser(filename)

    elif mode == Mode.Interactive:
        run_interactive()


if __name__ == "__main__":
    main()
