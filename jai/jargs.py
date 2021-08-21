from optparse import OptionParser
from jai.logger import Severity, log
import jai


def version():
    print(f"Jai {jai.__version__}")
    exit(0)


def get_args():
    ops = OptionParser()
    ops.add_option(
        "--version",
        action="store_true",
        dest="version",
        default=False,
        help="Get the version",
    )

    options, args = ops.parse_args()

    if options.version:
        version()

    filename = None
    if len(args) > 0:
        filename = args[0]
    else:
        log("Needed one argument for the filename", Severity.Fatal)

    return str(filename), options, args
