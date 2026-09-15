"""Starter code for the Python Text Processing assignment."""

import re
import sys


def normalize_text(text):
    """Return lowercase text with repeated whitespace collapsed."""
    raise NotImplementedError


def count_words(text):
    """Return the number of words in text."""
    raise NotImplementedError


def count_characters(text):
    """Return the number of non-whitespace characters in text."""
    raise NotImplementedError


def most_common_words(text, limit):
    """Return the most frequent words as (word, count) pairs."""
    raise NotImplementedError


def analyze_file(input_path, output_path):
    """Read input_path and write a text analysis report to output_path."""
    raise NotImplementedError


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python starter-code.py input.txt report.txt")

    analyze_file(sys.argv[1], sys.argv[2])