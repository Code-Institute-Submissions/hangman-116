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

    

rules()
