#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import random
print('Welcome to number guessing game! You have only 7 chances to guess the number.\n')
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num=random.randint(low,high)
chances = 7
guesses = 0
while(guesses<chances):
    guesses += 1
    guess = int(input('Guess a number between: '))

    if guess==num:
        print(f'Correct! The number is {num}. You guessed it in {guesses} attempt(s).')
        break
    elif guesses>=chances and guess!=num:
        print(f'Sorry! The number was {num}. Better luck next time.')
    elif guess > num:
        print('Too high! Try a lower number.')
    elif guess < num:
        print('Too low! Try a higher number.')


# In[ ]:




