from enum import Enum
from termcolor import colored


class Severity(Enum):
    Info = 0
    Debug = 1
    Warning = 2
    Error = 3
    Fatal = 4
    Raw = 5


def log(message: str, severity: Severity):
    # Print only the raw message
    if severity == Severity.Raw:
        print(message)
        return

    # Add the type of log before the message
    message = f"{severity.name}: {message}"

    # Change the color of the message if severity it high
    if severity == Severity.Warning:
        message = colored(message, "yellow")
    if severity == Severity.Error:
        message = colored(message, "red")
    if severity == Severity.Fatal:
        message = colored(message, "red")

    print(message)

    # Quit the program if the severity is fatal
    if severity == Severity.Fatal:
        exit(-1)
