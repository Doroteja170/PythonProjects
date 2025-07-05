# 21
# if sum>21 -> lose
# jack queen king =10
# ace =1 or 11
# we can draw a card if it's over 21 ->lose
# if deler=our ->draw
#
# if deler=21<our ->lose
# if deler<17 then must draw another card
# if deler>our ->lose

import random
from art import logo
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# print(logo)
answer=input(f"Do you want to play a game of BlackJack? Type 'y' or 'n': ")
while answer=='y':
    yours = []
    computer = []
    for i in range(2):
        yours.append(random.choice(cards))
        computer.append((random.choice(cards)))
    your_sum = yours[0] + yours[1]
    comp_sum = computer[0] + computer[1]
    print(f"Your cards: {yours} ")
    print(f'Computer first card: {computer[0]} ')
    another=input("Type 'y' to get another card, type 'n' to pass: ")
    while comp_sum < 17:
        new_card = random.choice(cards)
        computer.append(new_card)
        comp_sum += new_card
    if another=='y':
        yours.append(random.choice(cards))
        your_sum+=yours[2]
        if your_sum > 21 and 11 in yours:
            yours[yours.index(11)] = 1
            your_sum = sum(yours)
        print(f'Your final hand: {yours}')
        print(f'Computer final hand: {computer}')

    else:
        print(f'Your final hand: {yours}')
        print(f'Computer final hand: {computer}')
    if your_sum>21:
        print('You LOSE!')
    elif your_sum<=21 and comp_sum>21:
        print('You WIN!')
    elif your_sum==comp_sum:
        print('DRAW')
    elif your_sum<comp_sum and your_sum<=21 and comp_sum<=21:
        print('You LOSE!')
    elif your_sum>comp_sum and your_sum<=21 and comp_sum<=21:
        print('You WIN!')
    input('Do you want to play a game of BlackJack ("y", "n")?: ')
    if answer=='n':
        break
