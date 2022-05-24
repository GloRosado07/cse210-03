'''The responsibility of player is to solve a puzzle by 
    guessing the letters of a secret word one at a time.'''
class Player:
    def __init__(self, alive, lives):
        self._letter = " "   
        self.alive = alive
        self._lives = lives
    ''' Attributes: letter (str): The letter (a-z) that the player inputs.'''
    def _letter(self):
        self._letter = self._validate_input("Enter a letter from a-z: ").lower()
    
    def alive(self):
        self.alive = word 
        word = []
        if word == []:
            self._alive = True
        else:
             word != []
             self._alive = False
    def _lives(self, validate):
        life = 3
        self._lives = life   
        if not validate: 
            life -= 1 