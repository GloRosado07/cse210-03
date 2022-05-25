import re
'''The responsibility of player is to solve a puzzle by 
    guessing the letters of a secret word one at a time.'''
class Player:
    def __init__(self):
        self._letter = ''
        self.validation = ''
    ''' Attributes: letter (str): The letter (a-z) that the player inputs.'''
    def _get_letter(self):
        return self._letter
    def _set_letter(self, letter):
        self._letter = letter
        while not re.match('^[a-zA-Z]$', self._letter):
            print('The input must be an alphabet letter')
            self._letter = input("\nGuess a letter [a-z]: ")
        self.validation = self._letter

        



