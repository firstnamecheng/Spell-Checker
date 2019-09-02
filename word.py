"""
File name: word.py
Version: python 3.7
Author: Cheng Ye

A class representation of a word,
used to store punctuation and changes made to the word.
"""

from dataclasses import dataclass
from string import punctuation


@dataclass()
class Word:

    def __init__( self, s ):
        self.orig = s
        self.unchecked = ""
        self.front = ""
        self.end = ""
        self.corrected = ""

    def remove_punc( self ):
        """
        Runs a loop to remove all punctuation
        before and after a word.
        """
        f = 0
        while self.orig[ f ] in punctuation:
            f += 1

        e = len( self.orig ) - 1
        while self.orig[ e ] in punctuation:
            e -= 1

        self.unchecked = self.orig[ f: e + 1 ]
        self.front = self.orig[ : f ]
        self.end = self.end[ e + 1: ]

    def get_corrected( self ):
        """
        Returns the corrected word
        """
        return self.front + self.corrected + self.end

    def is_number( self ):
        """
        Returns true if word is a number
        """
        return self.word.isdigit()

    def get_unchecked( self ):
        return self.unchecked
