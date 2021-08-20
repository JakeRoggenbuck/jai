import jai
from jai import Lexer, Token, Settings, EMPTY_TOKEN
import jargs
from os.path import exists
from logger import Severity, log


def main():
    filename, options, args = jargs.get_args()
    current_token = EMPTY_TOKEN

    if not exists(filename):
        log("File does not exist", Severity.Fatal)

    with open(filename, "r") as file:
        lexer = Lexer(file.read(), Settings.PARSE_STRING)
        while current_token.token != Lexer.EOF:
            current_token = lexer.next()

            print(current_token)


if __name__ == "__main__":
    main()
