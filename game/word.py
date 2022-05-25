import random
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
        self._selected_word = ''
        self.hidden_word = ""
    def set_new_word(self):
        """
        Generates a random word from a list and
        save it in _selected_word, then calls
        the set_hidden_word method.
        """
        word_list = []
        with open('game/words.csv') as data:
            for i in data:
                word_list.append(i.rstrip())
        self._selected_word = random.choice(word_list)
        self._set_hidden_word()
        print(self._set_hidden_word())
    def get_word(self):
        """
        Getter for _selected_word attribute.
        """
        return self._selected_word

    def _set_hidden_word(self):
        """
        Set the number of letters in _selected_word as
        "_" in the hidden_word attribute.
        """
        self.hidden_word = ""
        for _ in self._selected_word:
            self.hidden_word += "_ "
        self.hidden_word = self.hidden_word [:-1]

    def letter_validation(self,letter):
        """
        Compares if the input letter is in _selected_word.
        If True, calls the _update_hidden_word method.

        Args:
            Letter: [String] letter to compare.

        Returns: Boolean
        """
        if letter in self._selected_word:
            self._update_hidden_word(letter)
            return True
        else:
            return False

    def _update_hidden_word(self,letter):
        """
        Check the input letter and update in
        hidden_word.
        Args:
            Letter: [String] letter to update.
        """
        tmpList = self.hidden_word.split(" ")
        for index, letter_word in enumerate(self._selected_word):
            if letter == letter_word:
                tmpList[index] = letter
        self.hidden_word = " ".join(tmpList)