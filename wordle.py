'''
Wordle: Text based game
@author - Sam Worthington
'''

import random

length_of_word = 5
max_num_guesses = 7 #This is 6 attempts. As guesses starts at 1

answers = []

#Reading all the potential answer words from a text file
file = open("wordle_answers.txt", "r")
for word in file:
    answers.append(word.strip())
file.close()

#Randomly selecting a word from the list 'answers'
answer = random.choice(answers).upper()

def analysis(guessed_word):
    '''
    This function returns the evaluation of the guessed word compared to the answer
    @param - guessed_word - is the user's guess word
    @return - returns the feedback of the guessed word in the format stated below:

    Feedback format:
    In word, in correct position = *
    In word, wrong position = ?
    Not in word = .
    '''
    feedback = ""
    letters = []

    for i in range(length_of_word):
        letters.append(guessed_word[i])

        #Checks if the letter is in the correct position
        if guessed_word[i] == answer[i]:
            feedback += "*"
            #Checks if the letter has already appeared in the word
            #Therefore, it replaces the the '?' with a '.'
            if letters.count(guessed_word[i]) > answer.count(guessed_word[i]):
                for index in range(0,len(letters)):
                    if letters[index] == guessed_word[i] and feedback[index] == "?":
                        feedback = feedback[0:index] + '.' + feedback[index+1:]
        
        #Checks if the letter is in the answer
        elif guessed_word[i] in answer and answer.count(guessed_word[i]) >= letters.count(guessed_word[i]):
            #Ensures that if a guessed word contains the same letter multiple times
            #checks to make sure not to duplicate '?' when comparing to the answer
            if answer.count(guessed_word[i]) < letters.count(guessed_word[i]):
                feedback += "."
            else:
                for j in range(length_of_word):
                    if answer[j] == guessed_word[i]:
                        feedback += "?"
                        break

        else:
            feedback += "."

    return feedback


def run():
    '''
    This function runs the game where the user inputs their guesses
    '''
    found_word = False
    guesses = 1

    print("\nEnter your guesses:\n")
    while not found_word and guesses != max_num_guesses:
        guess = input("").upper()

        if guess == answer:
            print("*****")
            print("\nCorrect: The word is",answer)
            if guesses == 1:
                print("It took you", guesses, "guess\n")
            else:
                print("It took you", guesses, "guesses\n")
            found_word = True

        else:
            results = analysis(guess)
            print(results,"\n")
            guesses += 1
    
    if guesses == max_num_guesses:
        print("Out of guesses. The word was: ", answer)


def settings():
    '''
    This function explains how to play the game of Wordle then returns
    back to the main menu method
    '''
    print('''
    Guess the WORDLE in six tries.

    Each guess must be a valid five-letter word. Hit the enter button to submit.

    After each guess, your will get given feedback. If you guess the word, you win!
    
    Example:
    
    If letter is in the word, in correct position = *
    If letter is in the word, wrong position = ?
    If letter is not in the word = .
    ''')

    main_menu()


def main_menu():
    '''
    This function is where the user can navigate
    around the game
    '''
    print("-----Wordle-----")
    print("1. Run Wordle")
    print("2. How to play")

    choice = int(input("Enter: "))

    if choice == 1:
        run()

    elif choice == 2:
        settings()

    else:
        print("\nInvalid Entry. Try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
