from parachute import parachute
from word import Word
# from player import player

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
        self._word = Word()
        self._play_game = True
        # self._player = Player()
        self._parachute = parachute()

    def start_game(self):
        '''
        Starts the game
        
        '''

        while self._play_game:
            self._do_output()
            self._get_input()
            self._do_update() 

    def _do_output(self):
        '''
        Ask the user for a letter
        Display the figure of the man with a parachute.
        '''
        self._word.get_word()
        self._parachute.__init__(self._word.cut_parachute())

   # def _get_input(self):
   #    ask_player = input("\nGuess a letter [a-z]: ")
   #     self._player.set_input(ask_player)

    def _do_update(self):

   #     self._word.letter_validation(self._player.get_input())
        self._parachute.__init__(self._word.cut_parachute())
        if self._word.letter_validation() == 1:
        
            '''
            It will keep asking the user for an input letter and display answer. 
            '''
            
   #         self._word.letter_validation(self._player.get_input())
            self._parachute.__init__(self._word.cut_parachute())
            
        if self._word.letter_validation() == 1 or self._word.cut_parachute() == 7:
            self._play_game = False


