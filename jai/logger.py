from enum import Enum


class Severity(Enum):
    Info = 0
    Debug = 1
    Warning = 2
    Error = 3
    Fatal = 4
    Raw = 5


def log(message: str, severity: Severity):
    if severity == Severity.Raw:
        print(message)
        return

    print(f"{severity.name}: {message}")

    if severity == Severity.Fatal:
        exit(-1)
