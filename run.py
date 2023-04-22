# Print the title of the game
print(
    f"""
 _    _                                        
| |  | |                                       
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                     __/ |                      
                    |___/    
    """)

print("Welcome to Hangman!")

def rules():
    """
    Displays rules of the game if user inputs 'y', otherwise does nothing.
    """
    show_rules = input("Do you want to display the rules? (y/n): \n")

    while show_rules.lower() not in ["y", "n"]:
        show_rules = input("Invalid input. Please enter 'y' to display the rules or 'n' to skip: \n")

    if show_rules.lower() == "y":
        print("First, you'll need to pick a name to play with.")
        print("Next, you'll choose a difficulty level: easy, medium, or hard.")
        print("The game will choose a word, and your job is to guess the letters in that word.")
        print("If you guess a letter correctly, it will be revealed in the word.")
        print("But if you guess incorrectly, part of a drawing of a 'hangman' will appear.")
        print("You win the game if you guess all the letters in the word before the hangman is fully drawn.")


def create_username():
    """
    Prompts the user to enter a username containing only letters and numbers, and returns it.
    """
    



rules()
