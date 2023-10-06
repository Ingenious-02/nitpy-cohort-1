import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "berry", "figma", "grape",
             "kiwi", "lemon", "mango", "orange", "papaya", "peach", "pear", "plum",
             "strawberry", "watermelon", "elephant", "giraffe", "kangaroo", "lion",
             "panda", "tiger", "zebra", "airplane", "bicycle", "car", "helicopter",
             "motorcycle", "submarine", "train", "truck", "computer", "keyboard",
             "monitor", "mouse", "printer", "smartphone", "tablet", "football",
             "basketball", "tennis", "volleyball", "badminton", "golf", "hockey"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with blanks for unrevealed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to display the hangman figure
def display_hangman(ATTEMPTS):
    hangman_figure = [
        "   ____",
        "  |    |",
        "  |    O",
        "  |   /|\\",
        "  |   / \\",
        "__|__"
    ]
    for i in range(ATTEMPTS):
        print(hangman_figure[i])

# Function to play the Hangman game
def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    ATTEMPTS = 6  # Number of allowed incorrect attempts

    while ATTEMPTS > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\n" + current_display)
        
        if current_display == word_to_guess:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            ATTEMPTS -= 1
            print(f"Wrong guess! You have {ATTEMPTS} attempts left.")
            display_hangman(6 - ATTEMPTS)
            if ATTEMPTS == 0:
                print("You lose!\nSorry, you're out of attempts. The word was:", word_to_guess)
                break

    play_again = input("Do you want to play again? (y = yes / n = no): ").lower()
    if play_again == "y":
        hangman()

if __name__ == "__main__":
    hangman()
