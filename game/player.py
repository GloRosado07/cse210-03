import re

class Player:
    '''The responsibility of player is to solve a puzzle by 
    guessing the letters of a secret word one at a time.
    Attributes:
    letter (str): The letter (a-z) that the player inputs.
    '''
    def __init__(self):
        self._letter = ''
        self.validation = ''
    
    def _get_letter(self):
        """
        Returns _letter value.
        """
        return self._letter

    def _set_letter(self, letter):
        """
        Set _letter value. A unique letter string-type required.
        """
        self._letter = letter
        while not re.match('^[a-zA-Z]$', self._letter):
            print('The input must be an alphabet letter')
            self._letter = input("\nGuess a letter [a-z]: ")
        self.validation = self._letter

        



