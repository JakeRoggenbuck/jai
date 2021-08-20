import jai
from jai import Lexer, Token, Settings, EMPTY_TOKEN
import jargs


def main():
    filename, options, args = jargs.get_args()

    print(f"Jai {jai.__version__}")

    current_token = EMPTY_TOKEN

    with open(filename, "r") as file:
        lexer = Lexer(file.read(), Settings.PARSE_STRING)
        while current_token.token != Lexer.EOF:
            current_token = lexer.next()

            print(current_token)


if __name__ == "__main__":
    main()
