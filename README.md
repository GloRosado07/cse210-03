# cse210-03
# Dynamic of the game
* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.
# Rules 
* Only choose one letter

## Classes:
### Joseph Perez
+ parachute 
    figure: string
-    render(): will render the parachute and the monkey
### Daniel Parra
- + word  
-    word: list
-    selected_word: random string from word list
### Gloria Rosado
- + player 
-    letter: string
-    alive: boolean
-    life_counter: int
### Jonathan Uribe and Thomas Villalobos
- + driver 
-    answer: string
-    game(): Will call methods in a loop
-   display(): string
-    update(): Check if player is alive or check logic