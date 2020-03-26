import atexit

from kvm_switcher.console_scripts.argument_parser import default
from kvm_switcher.dbus import Watcher


def main():
    args = default()
    if args.verbose:
        print("Verbose mode enabled.")

    watcher = Watcher(extra_monitor=args.extra_monitor, verbose=args.verbose)
    atexit.register(watcher.stop)

    watcher.run()
    input()
    if args.verbose:
        print("Closing down system.")


if __name__ == '__main__':
    main()
