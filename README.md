# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with the user having the option to read the rules or create a username and select a difficulty level, ranging from easy to hard.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen](/readme_images/home_screen.PNG)

[View Hangman live project here](https://hangmans-noose.herokuapp.com/)
- - -
## Table of Contents


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
* Letter input. User can input thir guess letter by letter to guess the hidden word.
* Incorrect guess tracking. Visuallly drawing a part of the hangman figure.
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

![Guess a letter](/readme_images/guess-a-letter.PNG)

* Correct Guess
    * If letter is guessed, "Correct" message displays green.

![Correct guess](/readme_images/correct-guess.PNG)

* Incorrect Guess
    * If letter is not guessed, "Incorrect" message displays red.

![Incorrect guess](/readme_images/incorrect-guess.PNG)

* User guesses the word correctly
    * Message that confirms hangman is beaten.

![Won game](/readme_images/win.PNG)

* User is out of guesses
    * Message that confirms a lost game.

![Lose](/readme_images/lose.PNG)

* Play again

![Play again](/readme_images/play-again.PNG)

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