import random
from art import logo
print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt=0
if difficulty=='easy':
    attempt=10
    print('You have 10 attempts remaining to guess the number')
elif difficulty=='hard':
    attempt=5
    print('You have 5 attempts remaining to guess the number')
else:
    print('Wrong input')
answer=random.randint(1,100)
guess=0

while answer!=guess:
    guess=int(input('Make a guess: '))
    if guess==answer:
        print(f'You WIN! The answer was {answer}')
    elif guess>answer:
        attempt=attempt-1
        if attempt == 0:
            print("You've run out of guesses, you LOSE!")
            print(f'The answer was {answer}')
            break
        print('Too high.')
        print('Guess again.')
        print(f"You have {attempt} attempts remaining to guess the number")
    else:
        attempt=attempt-1
        if attempt == 0:
            print("You've run out of guesses, you LOSE!")
            print(f'The answer was {answer}')
            break
        print('Too low.')
        print('Guess again.')
        print(f"You have {attempt} attempts remaining to guess the number")





"""
If 'hard' then You have 5 attempts remaining to guess the number
Make a guess:
Too high, Too low
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess

You've run out of guesses, you lose.

Easy = 10 attempts
You got it! The answer was number.
"""