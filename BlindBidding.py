
stop=True
bidders={}

while stop:
    name = input('What is your name: ')
    bid = int(input("What's your bid amount: "))
    bidders[name] = bid
    answer = input('Is there anyone else who wants to bid? (yes/no): ')
    if answer =='yes':
        print('\n'*100)
    else:
        print('\n'*100)
        max=0
        for key in bidders:
            if max<bidders[key]:
                max=bidders[key]
                bidder=key
                print(f"The winner is {bidder} with a bid of ${max}")
        stop=False


# fruits={'orange':9,'apple':5,'strawberry':8}
# max(fruits,key=fruits.get) --- it will print orange

