# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with the user having the option to read the rules or create a username and select a difficulty level, ranging from easy to hard.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen](/readme_images/home_screen.PNG)

[View Hangman live project here](https://hangmans-noose.herokuapp.com/)
- - -

## Table of Contents
### [How to play](#how-to-play-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to Play

In this implementation of Hangman, you will play against the computer. 
You will be prompted to choose a difficulty level (easy, medium, or hard), and the computer will randomly select a word from a list of words corresponding to that level. 
You will then have to guess the letters in the chosen word before the hangman is complete.

## Logic flowchart

![Flowchart](/readme_images/hangman_flowchart.PNG)

## User Experience (UX)

Hangman is a classic word guessing game that provides a simple yet entertaining user experience. The user is presented with a blank series of dashes that represent the letters of a mystery word. They have to guess the letters in the word, one at a time. With each correct guess, the letter is revealed in the corresponding position(s). However, with each incorrect guess, a part of a hangman's body is drawn. The user can guess until they either correctly guess the entire word or the hangman is fully drawn, resulting in a loss. The game is easy to learn and provides a good balance of challenge and reward. It is also a great way to improve vocabulary and spelling skills while having fun.

### User Stories

* First-time visitor goals
    * Understand how the game works. Clear instructions and what the objective of the game is.
    * Play the game. Once the user understands the game, they will likely want to play it.
    * Enjoy the experience. The hangman game should be engaging and fun for the user.

* Returning visitor goals
    * Continue playing. The returning visitor may have enjoyed playing the game and wants to play again.
    * Share with friends. Inviting friends to give the game a try.
    * Exploring new features, if there is any.

* Frequent user goals
    * Improving their speed and accuracy in guessing words.
    * Increasing the difficulty level of the game to challenge themselves.
    * Sharing the game with others or inviting friends to play.
    * Exploring new features, if there is any.

---

## Features

* Word selection. The game randomly selects a word from one of the three available predefined lists of words.
* Difficulty settings. The game offers three difficulty settings, easy, medium and hard.
* Visual interface. Appealing interface that is easy to navigate and understand.
* Letter input. User can input their guess letter by letter to guess the hidden word.
* Incorrect guess tracking. Visually drawing a part of the hangman figure.
* Win or loss detection. Detect when the player has either successfully guessed the entire word or made too many incorrect guesses and lost the game.
* Play again at the end of the game.

### Existing Features

* Intro screen
    * Displays logo and a welcome message.

![Intro Screen](/readme_images/intro.PNG)

* Rules
    * User can choose to display rules or skip them using "y" or "n".

![Rules](/readme_images/rules.PNG)

* Enter a username

![Username](/readme_images/username.PNG)

* Introduction message and difficulty setting

![Difficulty Setting](/readme_images/difficulty_setting.PNG)

* Promp user to make a guess

![Guess a letter](/readme_images/guess_a_letter.PNG)

* Correct Guess
    * If letter is guessed, "Correct" message displays green.

![Correct guess](/readme_images/correct_guess.PNG)

* Incorrect Guess
    * If letter is not guessed, "Incorrect" message displays red.

![Incorrect guess](/readme_images/incorrect_guess.PNG)

* User guesses the word correctly
    * Message that confirms hangman is beaten.

![Won game](/readme_images/win.PNG)

* User is out of guesses
    * Message that confirms a lost game.

![Lose](/readme_images/lose.PNG)

* Play again

![Play again](/readme_images/play_again.PNG)

## Features Left to Implement

* Additional words might be available.
* Different word topics
* Scoring system
* Two player option

---

## Design

* Colors
    * dark-orange
    * orange-red
    * red
    * green

* Flowchart
    * [Draw.io](http://draw.io/)

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Codeanywhere](https://app.codeanywhere.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.

## Testing 

CI Python Linter was used to test run.py, colors.py and hangman_art_words.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/run_linter_check.PNG)
</details>

<details>
<summary> colors.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/colors_linter_check.PNG)
</details>

<details>
<summary> hangman_art_words.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/hangman_art_words_linter_check.PNG)
</details>

## Manual Testing

The game was manually tested extensively using codeanywhere terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end. Testing of rules display, username input validation, select difficulty input validation, gallows ASCII image display, correct and incorrect answers and finally win or lose display and play again feature.



| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | -------------- | ----------- | ------------- | ---------- |
| Intro Screen   | To display logo and welcome message | None | As Expected | ![Intro Screen](/readme_images/intro.PNG) |
| Display Rules | To display rules or skip them using either "y" or "n" | Input "y" to display, input "n" to skip | As Expected | ![Display rules](/readme_images/rules.PNG) |
| Enter Username | To save username and use it in personalised messages | Input alphanumeric name | As Expected | ![Enter username](/readme_images/username.PNG) |
| Personalized message including username | To display personalized message | None | As Expected | ![Personalized message](/readme_images/difficulty_setting.PNG) |
| Select Difficulty   | To retrieve word from the selected difficulty option | Input easy, medium or hard | As Expected | ![Difficulty](/readme_images/difficulty_setting.PNG) |
| Guess a letter   | Prompts user to guess a letter | Input a letter guess | As Expected | ![Guess a letter](/readme_images/guess-a-letter.PNG) |
| Guess Correct   | To display correct, gallows with no penalty applied, a list of already guessed letters and updated hidden word | Guessed a correct letter | As Expected | ![Guess correct](/readme_images/correct_guess.PNG) |
| Guess Incorrect   | To display incorrect, gallows with penalty applied, a list of already guessed letters and updated hidden word | Guessed an incorrect letter | As Expected | ![Guess incorrect](/readme_images/incorrect_guess.PNG) |
| Guess Invalid   | To display a message saying to input a single letter | Invalid input such as e.g too many letters or a number | As Expected | ![Guess invalid](/readme_images/guess_invalid.PNG) |
| Guessed Already   | To display a message saying guessed already | Input a letter that was already tried  | As Expected | ![Guess invalid](/readme_images/guessed_already.PNG) |
| Hangman gallows   | To display and update hangman gallows | Input a letter guess  | As Expected | ![Gallows](/readme_images/gallows.PNG) |
| Win   | To display win message | Guess the word in less than six tries | As Expected | ![Win game](/readme_images/win.PNG) |
| Lose   | To display lose message | Fail to guess the word in six tries | As Expected | ![Lose game](/readme_images/lose.PNG) |
| Play Again   | To display play again | Choose "y" for yes and "n" to end the game | As Expected | ![Play again](/readme_images/play_again.PNG) |

## Input validation testing

* Display rules
    * Cannot continue with empty input
    * Must be "y" or "n"

![Rules validation](/readme_images/rules_validation.PNG)

* Enter username
    * Username cannot be empty
    * Username cannot contain spaces
    * Username must be alphanumeric
    * Username cannot contain special characters
    * Username cannot be longer than 20 characters

![Username validation](/readme_images/username_validation.PNG)

* Select difficuly
    * Cannot continue with empty input
    * Must be "easy", "medium" or "hard"

![Difficulty validation](/readme_images/difficulty_validation.PNG)

* Guess a letter
    * Cannot continue with empty input
    * Must be a single letter
    * Must be a letter

![Letter validation](/readme_images/letter_validation.PNG)

* Play again
    * Cannot continue with empty input
    * Must be "y" or "n"

![Play again validation](/readme_images/play_again_validation.PNG)

## Fixed Bugs

* There is a warning notice that informs the user that there is just one chance remaining if he reaches his fifth guess before attempting to use a last guess. This meant that even if the user correctly identified the final letter after receiving a warning after his fifth guess and so winning the game, the warning message would still appear.
* This bug was fixed in the play_game function which was refactored to keep track of the is_game_won function in the code that runs the warning, final chance message, which can be found in the commits history.
* This bug was indentified by playing the game multiple times and trying to get to all possible outcomes that a user might experience while playing the game.

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Hangman](https://hangmans-noose.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository hangman](https://github.com/Thomas-Tomo/hangman)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository hangman](https://github.com/Thomas-Tomo/hangman)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons.
* I gained more python concepts through Python for begginers written by Brady Ellison.
* Python 3.11.3 documentation.
* ANSI color documentation.
* MDN web docs for python [Documentation](https://developer.mozilla.org/en-US/docs/Glossary/Python).

### Content

* Hangman game.
* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
 * Slack community for encouragement.
