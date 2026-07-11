import random as rnd

logo = r"""
  ____                         _   _              _   _                 
 / ___| _   _  ___  ___ ___   | |_| |__   ___    | \ | |_   _ _ __ ___  
| |  _ | | | |/ _ \/ __/ __|  | __| '_ \ / _ \   |  \| | | | | '_ ` _ \ 
| |_| || |_| |  __/\__ \__ \  | |_| | | |  __/   | |\  | |_| | | | | | |
 \____| \__,_|\___||___/___/   \__|_| |_|\___|   |_| \_|\__,_|_| |_| |_|
"""
print(logo)

print("\nI'm thinking of a number between 1 and 100.\n")
x = rnd.randint(1, 100)
# print(x)

while True:
    level = input("\neasy or hard: ").lower()

    if level == "easy":
        print("You have 10 chances to guess the number.")
        r = 10
    elif level == "hard":
        print("You have 5 chances to guess the number.")
        r = 5
    else:
        print("Please enter either easy or hard")
        r = 0


    for i in range(r):
        u = int(input("\nguess a number"))

        if u > x:
            if i==r-1:
                print("*************** You Lose ***************")
                break
            else:
                print("Too high")
        elif u < x:
            if i==r-1:
                print("*************** You Lose ***************")
                break
            else:
                print("Too low")
        else:
            print("You guessed correctly ..... You Won")
            break

    k = input("\nYou want to continue (y/n): ")

    if k == "y":
        pass
    elif k == "n":
        break



