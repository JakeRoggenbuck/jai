import jai
from jai.logger import log, Severity


def input_wrapper():
    inputted = input("jai> ")
    print("")

    if inputted.upper() == "Q" or inputted.upper() == "QUIT":
        print("Bye!")
        exit(0)

    return inputted


def run_interactive():

    logo = f"""
       ___       _
      |_  |     (_)     |   Documentation: https://github.com/JakeRoggenbuck/jai/wiki
        | | __ _ _      |
        | |/ _` | |     |   Version: {jai.__version__}
    /\\__/ / (_| | |     |
    \\____/ \\__,_|_|     |
    """

    print(logo)

    while 1:
        line = input_wrapper()
        yield line
