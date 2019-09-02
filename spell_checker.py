"""
File name: spell_checker.py
Version: python 3.7
Author: Cheng Ye

Spell checks and corrects typos
"""

from dataclasses import dataclass
from word import Word

LEGAL_WORD_FILE = "./Assets/american-english.txt"
KEY_ADJACENCY_FILE = "./Assets/keyboard-letters.txt"


@dataclass()
class SpellChecker:

    def __init__( self ):
        self.english = None
        self.adjacent = None
        self.checked_words = ""
        self.unknown = list()

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

    def check_adjacent( self, word ):
        """
        Replaces each letter in word with an adjacent letter
        and checks in the new word is in the english dictionary
        """
        for i in range( len( word.get_unchecked() ) ):
            char = word.get_unchecked()[ i ]
            if char not in self.adjacent.keys():
                return False

            for adj in range( len( self.adjacent[ char ] ) ):
                copy = word.get_unchecked()
                copy = copy[ 0: i ] + adj + copy[ i + 1: ]
                if copy in self.english:
                    word.corrected = copy
                    return True

        return False

    def check_extra( self, word ):
        """
        Checks if there is an extra unnecessary character in the word
        """
        for i in range( len( word.get_unchecked() ) ):
            new_word = word.get_unchecked()[ 0: i ] + word.get_unchecked()[ i + 1: ]
            if new_word in self.english:
                word.corrected = new_word
                return True

        return False

    def check_missing( self, word ):
        """
        Checks if there is a missing character in the word
        """
        for index in range( len( word.get_unchecked ) + 1 ):
            part1 = word.get_unchecked()[ :index ]
            part2 = word.get_unchecked()[ index: ]
            for value in range( ord( "a" ), ord( "z" ) + 1 ):
                new_word = part1 + chr( value ) + part2
                if new_word in self.english:
                    word.corrected = new_word
                    return True

        return False
    
    def run_checks( self, word ):
        """
        First checks if a word is a number,
        Then checks if the lowercase version is in the dictionary,
        Then runs check_adjacent, check_extra, and check_missing.

        If all checks fail, then the unknown word is printed.
        """
        word.remove_punc()
        if word.is_number():
            self.checked_words += word.orig
        elif word.get_unchecked().lower() in self.english:
            self.checked_words += word.orig
        # Each check can take a while, so writing extra
        # elif statements saves time
        elif self.check_adjacent( word ):
            self.checked_words += word.get_corrected()
        elif self.check_extra( word ):
            self.checked_words += word.get_corrected()
        elif self.check_missing( word ):
            self.checked_words += word.get_corrected()
        else:
            self.unknown.append( word.orig )

    def run( self ):
        file = input( "Enter text file here: " )
        text = open( file )

        for line in text:
            words = line.split()


        text.close()