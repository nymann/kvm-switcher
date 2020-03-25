from argparse import Namespace, ArgumentParser, ArgumentTypeError


def default() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        dest="verbose",
                        help="Enables verbose mode",
                        const=True,
                        default=False,
                        type=str2bool,
                        nargs="?")

    return parser.parse_args()


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError('Boolean value expected.')
