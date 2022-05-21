import random
from collections import deque
class Word:
    """
    A secret word to be hidden for the player.
    The responsability of Word is to hold a secret word and show
    the number of letters from it.

    Attributes:
        _selected_word: [Private - String]
        hidden_wrd: [Public - String]
    """
    def __init__(self):
        """
        Constructs a new instance of Word.
        """
        self._selected_word = None
        self.hidden_word = ""
    
    def set_new_word(self):
        """
        Generates a random word from a list and
        save it in _selected_word.
        """
        word_list = []
        with open("game/words.csv", 'r') as data:
            for i in data:
                word_list.append(i)
        self._selected_word = random.choice(word_list)

    def get_word(self):
        """
        Getter for _selected_word attribute.
        """
        return self._selected_word

    def set_hidden_word(self):
        """
        Set the number of letters in _selected_word as
        "_" in the hidden_word attribute.
        """
        for _ in self._selected_word:
            self.hidden_word += "_ "
        self.hidden_word = self.hidden_word [:-1]
