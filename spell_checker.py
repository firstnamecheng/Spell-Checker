"""
File name: spell_checker.py
Version: python 3.7
Author: Cheng Ye

Spell checks and corrects typos
"""

from dataclasses import dataclass

LEGAL_WORD_FILE = "./Assets/american-english.txt"
KEY_ADJACENCY_FILE = "./Assets/keyboard-letters.txt"


@dataclass()
class SpellChecker:

    def __init__( self ):
        self.english = None
        self.adjacent = None

    def get_dictionary( self ):
        """
        Reads file and adds each word to a set.
        This will serve as the english dictionary.
        """
        f = open( LEGAL_WORD_FILE )
        self.english = set()
        for line in f:
            self.english.add( line.strip().lower() )
        f.close()

    def get_adjacent( self ):
        """
        Makes a python dictionary with each letter
        in the alphabet as keys, and value as a list of letters adjacent
        to it on the keyboard.

        :return: dict
        """
        f = open( KEY_ADJACENCY_FILE )
        self.adjacent = dict()
        for line in f:
            letter = line[ 0 ]
            others = line[ 1: ].split()
            self.adjacent[ letter ] = others
        f.close()


