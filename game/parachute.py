from collections import deque
from word import Word
class parachute:
    def __init__(self):
        self.parachute=deque([" ___","/___\\","\\   /"," \\ /","  O"," /|\\"," / \\"])
        self.attemps = 0
        self.words = Word()
    #Will render the parachute
    def render(self):
        for i in self.parachute:
            print(f" {i}")
        print("\n^^^^^^^")
    #Cut the parachute by parts
    def cut_parachute(self):
        self.attemps = len(self.parachute) - 3  
        self.parachute.popleft()
        if self.attemps - 3 <= 0:
            self.parachute[0] = "  x"