"""Caesar Cipher implementation

This module demonstartes the implementation of Caesar Cipher in Python 3.
From Wikipedia:
In cryptography, a Caesar cipher, also known as Caesar’s cipher, the shift cipher, Caesar’s code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

"""
import string


def _shift_letters(letters, shift_factor):
    return letters[shift_factor:] + letters[:shift_factor]


def _make_lookup(letters, key):
    shifted_letters = _shift_letters(letters, key)
    return dict(zip(letters, shifted_letters))


def _construct_encryption_lookup(key):
    lookup = _make_lookup(string.ascii_lowercase, key)
    lookup.update(_make_lookup(string.ascii_uppercase, key))
    return lookup


def caesar_cipher(plaintext, key):
    lookup = _construct_encryption_lookup(key)
    return ''.join((lookup[char] if char in string.ascii_letters else char for char in plaintext))
