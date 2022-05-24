from collections import deque
class parachute:
    def __init__(self):
        self.parachute=deque([" ___","/___\\","\\   /"," \\ /","  O"," /|\\"," / \\"])
        self.attemps = len(self.parachute) - 3
    #Will render the parachute
    def render(self):
        print(self.words._selected_word)
        for i in self.parachute:
            print(f" {i}")
        print("\n^^^^^^^")
    #Cut the parachute by parts
    def cut_parachute(self):
        self.parachute.popleft()
        self.attemps -= 1 
        if self.attemps <= 0:
            self.parachute[0] = "  x"
