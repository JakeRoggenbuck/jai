from optparse import OptionParser
import logger


def get_args():
    ops = OptionParser()
    options, args = ops.parse_args()

    filename = None
    if len(args) > 0:
        filename = args[0]
    else:
        logger.log("Needed one argument for the filename", logger.Severity.Fatal)

    return filename, options, args
