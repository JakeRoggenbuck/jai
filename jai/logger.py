from enum import Enum


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
    print(f"{severity.name}: {message}")

    # Quit the program if the severity is fatal
    if severity == Severity.Fatal:
        exit(-1)
