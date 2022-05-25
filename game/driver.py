from game.word import Word
from game.player import Player
from game.parachute import Parachute

class Driver:
    '''
    The Driver class will start the game. 
    
    '''
    def __init__(self) -> None:
        '''
        Atributes: 
        _word > to pick random word from a list of words. 
        _play_game > It will be used in a while loop to keep playing the game
        _player > It will ask the user for a letter. 
        _parachute > it create a figure of the man with a parachute. 
        
        '''
        self.word = Word()
        self.play_game = True
        self.player = Player()
        self.parachute = Parachute()
        self.bool = None
        self.ask_player = ''
        self.counter = 0
    def start_game(self):
        '''
        Starts the game
        
        '''
        self.word.set_new_word()

        while self.play_game:
            self.do_output()
            self.get_input()
            self.bool = self.word.letter_validation(self.ask_player)
            if not self.bool: 
                self.parachute.cut_parachute()
            self.do_update()
            


    def do_output(self):
        '''
        Display the figure of the man with a parachute.
        '''
        print(self.word.hidden_word)
        print()
        self.parachute.render()

    def get_input(self):
        '''
         Ask the user for a letter
        '''
        self.player._set_letter(input("\nGuess a letter [a-z]: "))
        self.ask_player = self.player.validation
    


    def do_update(self):

   #     self._word.letter_validation(self._player.get_input())
   #     self._parachute.__init__(self._parachute.cut_parachute())
   #     if self._word.letter_validation() == 1:
        
   #         '''
   #         It will keep asking the user for an input letter and display answer. 
   #         '''
            
   #         self._word.letter_validation(self._player.get_input())
   #        self._parachute.__init__(self._parachute.cut_parachute())
            
   #    if self._word.letter_validation() == 1 or self._parachute.cut_parachute() == 7:
   #         self._play_game = False

        '''
        It will keep continuing until the parachute disappears 
        '''
        
        if self.parachute.attemps <= 0:
            self.do_output()
            self.play_game = False
            print("Game Over")

