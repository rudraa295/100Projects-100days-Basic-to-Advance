import random

logo = r"""
.------.
|A_  _ |.
|( \/ ).----.
| \  /|K /\  |
|  \/ | /  \ |
'-----|\ \/ K|
      | \  / |
      |  \/  |
      '------'

 ____  _            _    _            _    
| __ )| | __ _  ___| | _(_) __ _  ___| | __
|  _ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|____/|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\
"""

print(logo)

cards = {
    "ACE": 11,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "JACK": 10,
    "QUEEN": 10,
    "KING": 10,
}


def picker():
    card = random.choice(list(cards.keys()))
    return card

def decision():

    while True:
        if sum(dealer) <= 16:
            dealer.append(cards[picker()])
            print(f"Dealer choose to get another card {dealer}")
        else:
            print("Dealer choose to pass")
            break

    if sum(dealer) > 21:
        print(f"You Won *** {mess()}")
        exit()
    elif sum(dealer) == 21:
        print(f"You Lose *** {mess()}")

    if sum(player) > sum(dealer):
        print(f"You Won *** {mess()}")
        exit()
    elif sum(player) < sum(dealer):
        print(f"You Lose *** {mess()}")
        exit()
    elif sum(player) == sum(dealer):
        print("*** next round ***")

def mess():
    return f"Dealer score is {sum(dealer)} {dealer}, current score is {sum(player)} {player}"


player = []
dealer = []


player.append(cards[picker()])
player.append(cards[picker()])
if 1 in player:
    if sum(player)<=11:
        player[player.index(1)] = 11
    else:
        pass

print(f'You have {player[0]} and {player[1]} : current score is {sum(player)}')


dealer.append(cards[picker()])
dealer.append(cards[picker()])
if 1 in dealer:
    if sum(dealer)<=11:
        dealer[dealer.index(1)] = 11
    else:
        pass

print(f'Dealer have {dealer[0]} and _')

if sum(player) == 21:
    print(f"Blackjack 🎉 .......... You Won .......... {mess()}")
    exit()

elif sum(dealer) == 21 and sum(player) == 21:
    print(f"***TIE***  {mess()}")
    exit()

elif sum(dealer) == 21:
    print(f"You Lose ....... {mess()}")
    exit()

else:
    pass


while True:

    inp = input("Type y to get another card or type n to pass : ").lower()


    if inp == "y":
        player.append(cards[picker()])

        if sum(player) > 21:
            print(f"***You Lose*** {mess()}")
            break
        elif sum(player) == 21:
            print(f"You Won *** {mess()}")
            break
        else:
            decision()

    elif inp == "n":
        decision()

    else:
        print("Please type y or n")















