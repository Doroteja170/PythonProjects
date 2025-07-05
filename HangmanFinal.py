word_list=['basketball','chair','magic']

import random
chosen_word=random.choice(word_list)
print(chosen_word)
print(len(chosen_word)*'_')

# TODO-1 Create variable lives to keep track of the lives. Set lives equal to 6
lives=6
correct=[]
while lives!=0 :
    guess = input('Guess a letter: ').lower()
    if(guess not in chosen_word):
        lives=lives-1
        print(f'Wrong guess! You have {lives} lives left')
        if(lives==0):
            print('Game Over!')
    else:
        display = ''
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct.append(guess)
            elif letter in correct:
                display+=letter
            else:
                display += '_'

        print(display)

        if display == chosen_word:
            print('You win!')
            exit()


