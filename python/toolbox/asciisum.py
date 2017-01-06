"""Print the ASCII sums of strings."""
import argparse


def asciisum(word):
    """Print the ASCII sums of strings."""
    print(sum(map(ord, word)))


def parse(args):
    """Setup the module's CLI parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="Word to convert")
    args = parser.parse_args(args)
    asciisum(args.word)
