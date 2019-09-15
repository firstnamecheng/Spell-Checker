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
        self.upper = False

    def preprocess( self ):
        """
        Runs a loop to remove all punctuation
        before and after a word.

        Checks if a word is capitalized or not.
        """
        f = 0
        while self.orig[ f ] in punctuation:
            f += 1

        e = len( self.orig ) - 1
        while self.orig[ e ] in punctuation:
            e -= 1

        self.front = self.orig[ : f ]
        self.end = self.orig[ e + 1: ]
        self.unchecked = self.orig[ f: e + 1 ]
        if self.unchecked[ 0 ] != self.unchecked[ 0 ].lower():
            self.unchecked = self.unchecked.lower()
            self.upper = True

    def set_corrected( self, new_word ):
        """
        Sets if the word is originally capitalized, recapitalize it.
        Sets corrected word.

        :param new_word: Corrected word
        """
        if self.upper:
            new_word = new_word[ 0 ].upper() + new_word[ 1: ]

        self.corrected = self.front + new_word + self.end

    def get_corrected( self ):
        """
        Returns the corrected word
        """
        return self.corrected

    def is_number( self ):
        """
        Returns true if word is a number
        """
        return self.unchecked.isdigit()

    def get_unchecked( self ):
        return self.unchecked
