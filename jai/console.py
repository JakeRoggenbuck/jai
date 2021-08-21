import jai
from jai.logger import log, Severity
from termcolor import colored

EXIT_MESSAGE = "Bye!"


def input_wrapper():
    try:
        inputted = input("jai> ")
        print("")

        if inputted.upper() == "Q" or inputted.upper() == "QUIT":
            print(EXIT_MESSAGE)
            exit(0)

    # This will gracefully leave if ctrl+c is done
    except KeyboardInterrupt:
        print(f"\n{EXIT_MESSAGE}")
        exit(0)

    return inputted


def run_interactive():
    line_1 = colored("   ___       _ ", "blue")
    line_2 = colored("  |_  |     (_)", "blue")
    line_3 = colored("    | | __ _ _ ", "blue")
    line_4 = colored("    | |/ _` | |", "blue")
    line_5 = colored("/\\__/ / (_| | |", "blue")
    line_6 = colored("\\____/ \\__,_|_|", "blue")

    lines = [line_1, line_2, line_3, line_4, line_5, line_6]
    # Add vertical line to lines 2-6
    lines = [line + "    |    " for line in lines[1:]]

    line_2, line_3, line_4, line_5, line_6 = lines
    # Add specific text after vertical lines
    line_2 += colored("Interactive mode!", "blue")
    line_3 += "Documentation: https://github.com/JakeRoggenbuck/jai/wiki"
    line_5 += f"Version: {colored(jai.__version__, 'green')}"
    line_6 += f"Authors: {jai.__author__}"

    lines = [line_1, line_2, line_3, line_4, line_5, line_6]
    # Add a newline to all lines 1-6
    lines = [line + "\n" for line in lines]

    # Join all the lines back into a block
    logo = "".join(lines)
    print(logo)

    while 1:
        line = input_wrapper()
        yield line
