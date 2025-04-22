# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 06:28:30 2025

@author: PIOTR
"""


import random


FRUITS = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
WORD_LIST = FRUITS.split(' ')



def choose_word(words):
    """
    Chooses a random worrd from al list.
    """
    return random.choice(words)


def try_guessing(word: str):
    """
    Guessing loop for one game.
    """
    guessed_letters = []
    is_it_won = False
    chances_left = 10
    
    while True:
        letter = input('Try to guess a letter:')
        
        if(not letter.isalpha()):
            print('This is not a letter.')
            continue
        
        elif(len(letter) > 1):
            print('This is more than one letter.')
            continue
            
        elif(letter in guessed_letters):
            print('You have already tried this letter.')
            continue
        
        if(letter in word): # Checking whether a letter is in word.
            print('Correct.')
            guessed_letters.append(letter)
            
            is_it_won = True
            for char in word: # Printing out the word
                if(char in guessed_letters):
                    print(char, end = ' ')
                else:
                    print('_', end = ' ')
                    is_it_won = False
            print('')
        
        else:
            print('Incorrect.')
            chances_left -= 1
            print('You have {} chance(s) left.'.format(chances_left))

            
        if(is_it_won): # Winning codition
            return True
        
        if(chances_left < 1): # Losing condition 
            return False
            
    return False


def ask_to_play_again() -> bool:
    """
    Asks if the player wants to play again.
    """
    answer = False
    
    while True:
        try:
            input_number = int(input('Press 0 to quit, 1 to play again: '))
            
            if(input_number == 0):
                answer = False
                break
            
            elif(input_number == 1):
                answer = True
                break
                
            else:
                print('This is not a valid option.')           
        
        except ValueError:
            print('This is not a number.')
        
    
    return answer
    


def main():
    """
    Main game function
    """
    
    print('This is a hangman game. You should try to guess a fruit.')

    play_again = True
    while play_again:
        word = choose_word(WORD_LIST)
        
        if(try_guessing(word)):
            print('You have won!')
            
        else:
            print('Not this time. You have lost.')
        
        play_again = ask_to_play_again()
    

if __name__ == "__main__":
    main()