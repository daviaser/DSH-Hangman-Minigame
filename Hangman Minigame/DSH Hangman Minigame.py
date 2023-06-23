import random
from Wordlist import words
from hangman_visual import lives_visual_dict
import string
import sys


def get_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while '-' in word or ' ' in word: # if '-' in word or string is empty, another word is chosen
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    lives = 7
    print("\nWelcome to DSH Hangman Minigame!!\n")
    
    # getting user input
    while len(word_letters) > 0 and (lives > 0):
        
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie P - N)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if letter is incorrect
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Choose another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You lost, sorry. The word was', word)
    else:
        print('YAY! Congrats! You guessed the word', word,'!!')
    
    f = input("\nDo you want to play again? ").lower()
    if f != "no":
        hangman()
    else:
        print("\nOkay, Thank you for playing!! Until next time!!")
        exit()
    
    

if __name__ == '__main__':
    hangman()