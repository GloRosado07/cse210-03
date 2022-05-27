from collections import deque
class Parachute:
    """
    The responsability of Parachute is to render the parachute
    in the terminal and follow the player attemps.
    Attributtes:
        Parachute: [public - list]
        Attemps: [public - int]
    """
    def __init__(self):
    #Constructs an instance of Parachute
        self.parachute=deque([" ___","/___\\","\\   /"," \\ /","  O"," /|\\"," / \\"])
        self.attemps = len(self.parachute) - 3

    #Will render the parachute
    def render(self):
        for i in self.parachute:
            print(f" {i}")
        print("\n^^^^^^^")

    #Cut the parachute by parts
    def cut_parachute(self):
        self.parachute.popleft()
        self.attemps -= 1 
        if self.attemps <= 0:
            self.parachute[0] = "  x"