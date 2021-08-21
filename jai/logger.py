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
    message_type = f"{severity.name}"

    # Change the color of the message if severity it high
    if severity == Severity.Warning:
        message_type = colored(message_type, "yellow")
    elif severity == Severity.Error:
        message_type = colored(message_type, "red")
    elif severity == Severity.Fatal:
        message_type = colored(message_type, "red")

    message = f"{message_type}: {message}"
    print(message)

    # Quit the program if the severity is fatal
    if severity == Severity.Fatal:
        exit(-1)
