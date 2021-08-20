from enum import Enum


class Severity(Enum):
    Info = 0
    Warning = 1
    Error = 2
    Fatal = 3


def log(message: str, severity: Severity):
    print(f"{severity.name}: {message}")

    if severity == Severity.Fatal:
        exit(-1)
