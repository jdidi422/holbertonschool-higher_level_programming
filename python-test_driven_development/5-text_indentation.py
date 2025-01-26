#!/usr/bin/python3
"""
This module provides a function that prints a text without indentation

Examples:
>>> text_indentation = __import__('5-text_indentation').text_indentation
>>> text_indentation("Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor
an totas paginas commovere? Non autem hoc: igitur ne illud quidem.")
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Quonam modo?

Utrum igitur tibi litteram videor an totas paginas commovere?

Non autem hoc:

igitur ne illud quidem.
>>> text_indentation("This is a test. It works well. Does it? Yes.")
This is a test.

It works well.

Does it?

Yes.
>>> text_indentation("Hello world: this is a test.")
Hello world:

this is a test.
>>> text_indentation(123)
Traceback (most recent call last):
    ...
TypeError: text must be a string
>>> text_indentation("")
Traceback (most recent call last):
    ...
TypeError: text must be a string
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
    text (str): The input string.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(text, str) or text == "":
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in '.?:':
            print("\n")
            while i + 1 < length and text[i + 1] == " ":
                i += 1
        i += 1
