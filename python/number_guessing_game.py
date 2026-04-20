{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "67905ba9-9341-402e-b467-8c488e67c313",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to number guessing game! You have only 7 chances to guess the number.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the lower bound:  10\n",
      "Enter the upper bound:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "You have 7 chances to guess the number between 10 and 20. Let's start!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess a number between:  16\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct! The number is 16. You guessed it in 1 attempts.\n"
     ]
    }
   ],
   "source": [
    "# import random\n",
    "print('Welcome to number guessing game! You have only 7 chances to guess the number.\\n')\n",
    "low = int(input(\"Enter the lower bound: \"))\n",
    "high = int(input(\"Enter the upper bound: \"))\n",
    "print(f\"\\nYou have 7 chances to guess the number between {low} and {high}. Let's start!\")\n",
    "\n",
    "num=random.randint(low,high)\n",
    "chances = 7\n",
    "guesses = 0\n",
    "while(guesses<chances):\n",
    "    guesses += 1\n",
    "    guess = int(input('Guess a number between: '))\n",
    "    \n",
    "    if guess==num:\n",
    "        print(f'Correct! The number is {num}. You guessed it in {guesses} attempt(s).')\n",
    "        break\n",
    "    elif guesses>=chances and guess!=num:\n",
    "        print(f'Sorry! The number was {num}. Better luck next time.')\n",
    "    elif guess > num:\n",
    "        print('Too high! Try a lower number.')\n",
    "    elif guess < num:\n",
    "        print('Too low! Try a higher number.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44f7254a-60dd-4961-ae9b-cb56010bf518",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
