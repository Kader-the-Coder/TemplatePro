"""
provides utility functions for clipboard operations.
"""

import pyperclip


def copy(text):
    """Copies the given text to the clipboard."""
    print(f"\"{text}\" copied to clipboard.")
    pyperclip.copy(text)
