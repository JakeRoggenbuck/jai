from optparse import OptionParser
from jai.logger import Severity, log
import jai
from jai.mode import Mode


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

    ops.add_option(
        "-o",
        "--outfile",
        dest="outfile",
        default=False,
        help="Set the output file",
    )

    ops.add_option(
        "-d",
        "--dont_write",
        action="store_true",
        dest="dont_write",
        default=False,
        help="Outputs the code gen",
    )

    options, args = ops.parse_args()

    if options.version:
        version()

    mode = Mode.NotSet
    filename = ""

    if len(args) > 0:
        filename = str(args[0])
        mode = Mode.Filemode
    else:
        mode = Mode.Interactive

    return mode, filename, options, args
