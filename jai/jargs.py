from optparse import OptionParser
from logger import Severity, log


def get_args():
    ops = OptionParser()
    options, args = ops.parse_args()

    filename = None
    if len(args) > 0:
        filename = args[0]
    else:
        log("Needed one argument for the filename", Severity.Fatal)

    return filename, options, args
