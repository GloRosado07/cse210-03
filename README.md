# cse210-03
Encapsulation: Demonstrate how encapsulation works on a program that controls access to class members.

# Libraries used: 
* Deque
* Random

# Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. 

# Jumper Game
* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.


# Contributors 

## Joseph Perez
- parachute 
1. figure: string
2. render(): will render the parachute and the monkey
  per16068@byui.edu
  
## Daniel Parra
- word  
1. _selected_word: string, private 
2. hidden_word: string, public
3. set_new_word(): creates a new word from word list
4. letter_validation(letter): compares letter with selected_word
5. get_word(): returns _selected_word. 
  par21002@byui.edu
  
## Gloria Rosado
- player 
1. letter: string
2. alive: boolean
3. life_counter: int
  ros21035@byui.edu
## Jonathan Uribe and Thomas Villalobos
- driver 
1. answer: string
2. game(): Will call methods in a loop
3. display(): string
4. update(): Check if player is alive or check logic
  u266801382@byui.edu and vil22003@byui.edu

# Project Structure

    main.py (program entry point)
    game folder (Game structure on different classes)

# Required Software
    Python 3.8.0


  

      
   
    

