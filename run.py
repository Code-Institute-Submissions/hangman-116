import hangman_art_words
import random

# Print the title of the game
print(" _    _")
print("| |  | |")
print("| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
print("|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\")
print("| |  | | (_| | | | | (_| | | | | | | (_| | | | |")
print("|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|")
print("                     __/ |")
print("                    |___/")


def rules():
    """
    Displays rules of the game if user inputs 'y', otherwise does nothing.
    """
    show_rules = input("Do you want to display the rules? (y/n):\n")

    while show_rules.lower() not in ["y", "n"]:
        show_rules = input("Enter 'y' to show rules or 'n' to skip:\n")

    if show_rules.lower() == "y":
        print("Pick a name to play with.")
        print("Choose a difficulty level (easy, medium, or hard).")
        print("Guess the letters in the chosen word.")
        print("Correct guess reveals letter; incorrect guess adds to hangman.")
        print("Win by guessing all letters before hangman is complete.")


def create_username():
    """
    Prompts the user to enter a username containing only letters and numbers,
    and returns it.
    """
    while True:
        try:
            name = input("Enter your name please:\n")
            # Check if the input is empty or only contains whitespace
            if not name.strip():
                raise ValueError("Please enter a valid username.")
            # Check if the input contains only letters and numbers
            if not name.isalnum():
                raise ValueError("Username must use only letters and numbers.")
            # Check if the input is longer than 20 characters
            if len(name) > 20:
                raise ValueError("Username must not exceed 20 characters.")
        # Catch any ValueError exception and print the error message
        except ValueError as e:
            print(f"{e}")
        else:  # If no exception is raised, print a message and return the name
            print(f"The noose awaits you {name.upper()}!")
            return name


def select_difficulty_level():
    """
    Prompts the user to choose a difficulty level
    and returns the corresponding word list.
    """
    while True:
        try:
            level = input("Select difficulty: easy, medium, or hard\n").lower()
            if level not in ["easy", "medium", "hard"]:
                raise ValueError("Invalid input. Choose easy, medium, hard\n")
            break
        except ValueError as e:
            print(e)

    # Return the appropriate word list based on the chosen difficulty level.
    if level == "easy":
        return hangman_art_words.easy_words
    elif level == "medium":
        return hangman_art_words.medium_words
    else:
        return hangman_art_words.hard_words


def choose_random_word(word_list):
    """
    Returns a randomly selected word from the given word list.
    """
    word = random.choice(word_list)
    return word.lower()


def handle_input(guessed_letters):
    """
    Handles user input and returns a lowercase letter
    that has not been guessed before.
    """
    while True:
        try:
            guess = input("Guess a letter:\n").lower()
            if len(guess) != 1:
                raise ValueError("Invalid input. Please enter a single letter")
            elif guess in guessed_letters:
                raise ValueError("You already guessed that letter. Try again.")
            elif not guess.isalpha():
                raise ValueError("Invalid input. Please enter a letter")
            else:
                return guess
        except ValueError as e:
            print(e)


def update_hidden(guess, secret_word, hidden_word):
    """
    Updates the hidden word with the given guess, based on the secret word.
    """

    # If the guessed letter is in the secret word,
    # iterate over the indices of the secret word
    if guess in secret_word:
        for i in range(len(secret_word)):
            # If the character at the current index matches the guessed letter,
            # update the hidden word at that index
            if secret_word[i] == guess:
                hidden_word[i] = guess
    # Return the updated hidden word
    return hidden_word


def is_game_won(hidden_word):
    """
    Returns True if the game is won
    (i.e., there are no more blank spaces in the hidden word).
    """
    return "_" not in hidden_word


def display_game_info(num_wrong_guesses, guessed_letters, hidden_word):
    """
    Displays the game information, including the hangman art,
    guessed letters, and current state of the hidden word.
    """
    print(hangman_art_words.hangman_art[num_wrong_guesses])
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(" ".join(hidden_word))


def play_game(name):
    """
    Runs the main game loop, where the user tries to guess the secret word.
    """

    # Game initialization
    while True:
        word_list = select_difficulty_level()
        secret_word = choose_random_word(word_list)
        hidden_word = ["_" for _ in secret_word]
        print(" ".join(hidden_word))

        num_wrong_guesses = 0
        guessed_letters = []

        # Main game loop
        while not is_game_won(hidden_word) and num_wrong_guesses < 6:
            guess = handle_input(guessed_letters)
            guessed_letters.append(guess)

            # Update game state and display game info
            if guess in secret_word:
                print("Correct!")
                hidden_word = update_hidden(guess, secret_word, hidden_word)
            else:
                print("Incorrect.")
                num_wrong_guesses += 1

            display_game_info(num_wrong_guesses, guessed_letters, hidden_word)

            if num_wrong_guesses == 5:
                print(f"Warning: final chance {name.capitalize()}!")

        # End of game: check if player won or lost
        if is_game_won(hidden_word):
            print("You've beaten the hangman.")
            print(f"Your name is clear {name.upper()}!")
            print("You are free to go!")
        else:
            print(f"You lost {name.upper()}. The word was:", secret_word)

        # Ask if player wants to play again
        if not play_again():
            break


def play_again():
    """
    Asks the player if they want to play again,
    and returns True if they do, False otherwise.
    """
    while True:
        try:
            play_again_input = input("Play again? (y/n):\n").lower()
            if play_again_input not in ['y', 'n']:
                raise ValueError("Invalid input. Please enter 'y' or 'n'.\n")
            break
        except ValueError as e:
            print(e)

    if play_again_input == "n":
        print("Thanks for playing!")
        return False
    else:
        return True


def main():
    """
    This function runs the main game loop for Hangman.
    It first displays the rules of the game,
    prompts the player to enter a username, and then starts the game.
    The game consists of the player trying to guess a randomly chosen
    word by suggesting letters one by one.
    If the player guesses a letter correctly, it is revealed in the word.
    If they guess incorrectly, part of a
    drawing of a "hangman" is displayed.
    The player wins the game if they guess all the letters
    in the word before the hangman is fully drawn.
    """
    rules()
    name = create_username()
    print("This is your only chance to beat the gallows.")
    print("Are you ready to play? Let's get started!")
    play_game(name)


if __name__ == "__main__":
    main()
