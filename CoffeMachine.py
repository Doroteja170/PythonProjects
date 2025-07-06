MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100
        },
        "cost":3.0
    }
}

# for key in MENU:
#     print(key)
#     print(MENU[key]['cost'])
#     for i in MENU[key]['ingredients']:
#         print(i)
#         print(MENU[key]['ingredients'][i])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# water=300
# milk=200
# coffee=100
money=0
turnoff=True

while turnoff:
    order=input("What would you like(espresso/latte/cappuccino): ").lower()
    if order=='report':
        for resource in resources:
            print(f'{resource.capitalize()}: {resources[resource]}')
        print(f'Money: {money}')
    elif order in MENU:
        ingredients = MENU[order]['ingredients']
        can_make=True
        for ingredient in ingredients:
            if resources[ingredient] < ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    can_make=False
        if can_make:
            print('Please insert coins: ')
            quarter=int(input("How many quarters?: "))
            dime=int(input("How many dimes?: "))
            nickle=int(input("How many nickles?: "))
            pennie=int(input("How many pennies?: "))

            total=(quarter*0.25)+(dime*0.1)+(nickle*0.05)+(pennie*0.01)
            change=total-MENU[order]["cost"]

            if change>=0:
                print(f'Here is {round(change,2)}$ in change.')
                print(f'Here is your {order}☕.Enjoy!')
                for leftover in ingredients:
                    resources[leftover]=resources[leftover]-ingredients[leftover]
                money=money+MENU[order]["cost"]

            else:
                print("Sorry that's not enough money. Money refunded.")
    elif order=='off':
        turnoff=False
    else:
        print('Invalid input. Try again.')





