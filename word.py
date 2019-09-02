"""
File name: word.py
Version: python 3.7
Author: Cheng Ye

A class representation of a word,
used to store punctuation and changes made to the word.
"""

from dataclasses import dataclass


@dataclass()
class Word:

    def __init__( self, string ):
        self.orig = string
        self.front = ""
        self.end = ""
        self.corrected = ""

