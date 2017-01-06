#!/usr/bin/env python3 import argparse


def discover(name):
    """Discover a sister module by name.

    Returns:
        ``module``: Python module or ``None``.
    """
    import importlib
    try:
        return importlib.import_module("toolbox." + name)
    except ImportError:
        return None


def available():
    import os
    import sys
    toolbox = sys.modules["toolbox"]
    mods = []
    for f in os.listdir(toolbox.__path__[0]):
        if not f.startswith('_') and f.endswith(".py"):
            mods.append(f.rstrip(".py"))
    return """toolbox <tool> <tool args>
    Available Tools:\n\t{}
    """.format("\n\t".join(mods))


def main():
    import argparse
    parser = argparse.ArgumentParser(usage=available())
    parser.add_argument("name", help="Utility name")
    parser.add_argument("args", nargs="*", help="Utility arguments")

    args = parser.parse_args()

    utility = discover(args.name)
    if utility:
        utility.parse(args.args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
