import random
from higherlowerart import logo, vs,over
items = {
    "Instagram, Social media platform": 690_000_000,
    "Cristiano Ronaldo, Footballer": 660_000_000,
    "Lionel Messi, Footballer": 505_000_000,
    "Selena Gomez, Musician and actress": 419_000_000,
    "Kylie Jenner, Media personality": 393_000_000,
    "Dwayne Johnson, Actor and wrestler": 393_000_000,
    "Ariana Grande, Musician and actress": 375_000_000,
    "Kim Kardashian, Media personality": 356_000_000,
    "Beyoncé, Musician and actress": 311_000_000,
    "Khloé Kardashian, Media personality": 302_000_000,
    "Nike, Sportswear multinational": 300_000_000,
    "Justin Bieber, Musician": 294_000_000,
    "Kendall Jenner, Media personality": 287_000_000,
    "Taylor Swift, Musician": 281_000_000,
    "National Geographic, Magazine": 278_000_000,
    "Virat Kohli, Cricketer": 273_000_000,
    "Jennifer Lopez, Musician and actress": 248_000_000,
    "Neymar, Footballer": 230_000_000,
    "Nicki Minaj, Musician": 225_000_000,
    "Kourtney Kardashian, Media personality": 218_000_000,
    "Miley Cyrus, Musician and actress": 212_000_000,
    "Katy Perry, Musician": 204_000_000,
    "Zendaya, Actress and singer": 178_000_000,
    "Kevin Hart, Comedian and actor": 177_000_000,
    "Real Madrid CF, Football club": 176_000_000,
    "Cardi B, Musician and actress": 163_000_000,
    "LeBron James, Basketball player": 159_000_000,
    "Demi Lovato, Musician and actress": 153_000_000,
    "Rihanna, Musician": 149_000_000,
    "Chris Brown, Musician": 144_000_000,
    "Drake, Musician": 142_000_000,
    "FC Barcelona, Football club": 141_000_000,
    "Ellen DeGeneres, Comedian and television host": 136_000_000,
    "Billie Eilish, Musician": 124_000_000,
    "Kylian Mbappé, Footballer": 124_000_000,
    "UEFA Champions League, Club football competition": 121_000_000,
    "Gal Gadot, Actress": 108_000_000,
    "Lisa, Musician": 106_000_000,
    "Vin Diesel, Actor": 103_000_000,
    "NASA, Space agency": 96_400_000,
    "Narendra Modi, Prime Minister of India": 95_900_000,
    "Shraddha Kapoor, Actress": 93_700_000,
    "Shakira, Musician": 92_500_000,
    "Priyanka Chopra, Actress": 92_300_000,
    "NBA, Professional basketball league": 90_700_000,
    "Snoop Dogg, Musician": 88_300_000,
    "David Beckham, Former footballer": 88_100_000,
    "Dua Lipa, Musician": 87_600_000,
    "Jennie, Musician": 87_300_000
}


score=0
correct=True
name=[]
for key in items:
    name.append(key)


A = random.choice(name)
B = random.choice(name)
while B == A:
    B = random.choice(name)

print(logo)
while correct:
    print(f'Compare A: {A}')
    print(vs)
    print(f'Against B: {B}')
    answer=input('Who has more Instagram followers A or B?: ')
    if items[A]>items[B] and answer=='A':
        score+=1
        print(40 * '\n')
        print(f'You are right! Current score: {score}')
    elif items[A]<items[B] and answer=='B':
        score+=1
        print(40*'\n')
        print(f'You are right! Current score: {score}')
    else:
        print(40*'\n')
        print(over)
        print(f"Sorry, that's wrong. Final score: {score}")
        correct=False
    A=B
    B = random.choice(name)
    while B == A:
        B = random.choice(name)
