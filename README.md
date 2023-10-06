# nitpy-cohort-1
NitHub University of Lagos Python Course Cohort 1.

My name is Ibraheem. This is a repository for my NITPY course and project.

Certainly! Below is a comprehensive documentation for the Hangman game, covering its concept, structure, user input, variables, data types, functions, error handling, user input validation, and other necessary details.

# Hangman Game Documentation

## Game Concept and Structure

**Hangman** is a classic word-guessing game where one player thinks of a word, and the other player tries to guess it by suggesting letters one at a time. The player has a limited number of attempts to guess the word correctly. For each incorrect guess, a part of a "hangman" figure is drawn. The player wins if they guess the word before the hangman figure is completed or loses if they run out of attempts.

### Game Structure

1. **Initialization**:
   - The game starts with a random word chosen from a predefined list.
   - The player is given a limited number of attempts (e.g., 6) to guess the word.

2. **Game Loop**:
   - The player is presented with blanks representing the letters in the word.
   - The player guesses one letter at a time.
   - If the guessed letter is in the word, it is revealed in its correct position(s) in the word.
   - If the guessed letter is not in the word, the player loses an attempt.
   - The game continues until the player guesses the word or runs out of attempts.

3. **Winning/Losing**:
   - The player wins if they correctly guess the entire word before running out of attempts.
   - The player loses if they run out of attempts, and the full "hangman" figure is drawn.

4. **Restart**:
   - After each game, the player has the option to play again.

## User Input

The player interacts with the game by providing input through the keyboard. The primary user inputs are as follows:

- Guessing a letter: The player enters a single letter (a-z) to guess a letter in the word.
- Play again: After a game is over, the player can choose to play another round.

## Variables and Data Types

The game uses the following variables and data types:

- `word_list` (list): A predefined list of words from which a random word is chosen for each game.
- `word_to_guess` (str): The word that the player is trying to guess.
- `guessed_letters` (list): A list to store the letters that the player has guessed.
- `attempts` (int): The number of remaining attempts.
- `guess` (str): The letter guessed by the player.
- `play_again` (str): Player's choice to play another round.

## Functions

### `choose_word()`

- Description: Chooses a random word from the `word_list` for the current game.
- Input: None
- Output: A random word (str)

### `display_word(word, guessed_letters)`

- Description: Displays the current state of the word with blanks for unrevealed letters.
- Input:
  - `word` (str): The word to display.
  - `guessed_letters` (list): List of guessed letters.
- Output: The word with blanks and guessed letters (str)

### `hangman()`

- Description: The main game loop that manages the gameplay.
- Input: None
- Output: None

### `main()`

- Description: The entry point of the program. Initializes and starts the game.
- Input: None
- Output: None

## Error Handling and User Input Validation

- If the player enters more than one letter or a non-alphabet character when guessing a letter, they are prompted to enter a single valid letter.

- The player is informed if they have already guessed a letter.

## Other Details

- The game provides feedback on correct and incorrect guesses.

- The player can play multiple rounds by choosing to play again after each game.

- The game uses a predefined list of words, but additional words can be added to the `word_list` for variety.

- The game loop continues until the player decides to exit.

- The game uses a simple hangman figure to represent incorrect guesses.

- The game can be customized by modifying parameters such as the number of attempts, the list of words, or the hangman figure.

This Hangman game is a fun and interactive way to test your word-guessing skills while enjoying a classic game.

## Documentation
