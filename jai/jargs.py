from optparse import OptionParser


def get_args():
    ops = OptionParser()
    options, args = ops.parse_args()

    filename = None
    if len(args) > 0:
        filename = args[0]
    else:
        # TODO: Setup errors
        print("Needed one argument for the filename")
        exit(-1)

    return filename, options, args
