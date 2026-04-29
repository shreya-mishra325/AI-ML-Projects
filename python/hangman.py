import random
from collections import Counter

someWords='''apple banana mango orange strawberry 
blueberry grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords=someWords.split(' ')
word=random.choice(someWords)

if __name__=='__main__':
    print('Guess the word! The word is a fruit')
    for _ in word:
        print('_', end=' ')
    print()
    letterGuessed = ''
    chances = len(word)+2
    flag=0

    try:
        while chances>=0 and flag==00:
            print()
            chances -= 1

            try:
                guess=input('Enter a letter to guess: ').lower()
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter')
                continue
            elif guess in letterGuessed:
                print('You already guessed that letter!')
                continue

            if guess in word:
                letterGuessed += guess*word.count(guess)
                
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print('\nYou lost! The word was:', word)

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
        exit()