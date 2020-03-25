from kvm_switcher.console_scripts.argument_parser import default


def main():
    args = default()
    if args.verbose:
        print("Verbose mode enabled.")
    print("Goodbye")


if __name__ == '__main__':
    main()
