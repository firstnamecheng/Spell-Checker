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
            letters = line.split()
            self.adjacent[ letters[ 0 ] ] = letters[ 1: ]

        f.close()

    def check_adjacent( self, u_word ):
        """
        Replaces each letter in word with an adjacent letter
        and checks in the new word is in the english dictionary
        """
        for i in range( len( u_word.get_unchecked() ) ):
            char = u_word.get_unchecked()[ i ]
            if char not in self.adjacent.keys():
                return False

            for adj in self.adjacent[ char ]:
                copy = u_word.get_unchecked()
                copy = copy[ 0: i ] + adj + copy[ i + 1: ]
                if copy in self.english:
                    u_word.set_corrected( copy )
                    return True

        return False

    def check_extra( self, u_word ):
        """
        Checks if there is an extra unnecessary character in the word
        """
        for i in range( len( u_word.get_unchecked() ) ):
            new_word = u_word.get_unchecked()[ 0: i ] + u_word.get_unchecked()[ i + 1: ]
            if new_word in self.english:
                u_word.set_corrected( new_word )
                return True

        return False

    def check_missing( self, u_word ):
        """
        Checks if there is a missing character in the word
        """
        for index in range( len( u_word.get_unchecked() ) + 1 ):
            part1 = u_word.get_unchecked()[ :index ]
            part2 = u_word.get_unchecked()[ index: ]
            for value in range( ord( "a" ), ord( "z" ) + 1 ):
                new_word = part1 + chr( value ) + part2
                if new_word in self.english:
                    u_word.set_corrected( new_word )
                    return True

        return False
    
    def run_checks( self, u_word ):
        """
        First checks if a word is a number,
        Then checks if the lowercase version is in the dictionary,
        Then runs check_adjacent, check_extra, and check_missing.

        If all checks fail, then the unknown word is printed.

        :param u_word: Unchecked word
        """
        u_word.preprocess()

        if u_word.is_number():
            self.checked_words += u_word.orig
        elif u_word.get_unchecked().lower() in self.english:
            self.checked_words += u_word.orig
        # Each check can take a while, so writing extra
        # elif statements saves time
        elif self.check_missing( u_word ):
            self.checked_words += u_word.get_corrected()
        elif self.check_adjacent( u_word ):
            self.checked_words += u_word.get_corrected()
        elif self.check_extra( u_word ):
            self.checked_words += u_word.get_corrected()
        else:
            self.unknown.append( u_word.orig )
            self.checked_words += u_word.orig

        self.checked_words += " "

    def run( self ):
        """
        Reads from the input file and starts spell checking.
        """
        self.get_adjacent()
        self.get_dictionary()

        file = input( "Enter text file here: " )
        text = open( file )

        for line in text:
            strings = line.split()
            for s in strings:
                u_word = Word( s )
                self.run_checks( u_word )

            self.checked_words += "\n"

        text.close()

        new_file = open( "checked_words.txt", "w+" )
        new_file.write( self.checked_words )
        new_file.close()
        print( "Unknown words:", self.unknown )


if __name__ == "__main__":
    spell_checker = SpellChecker()
    spell_checker.run()
