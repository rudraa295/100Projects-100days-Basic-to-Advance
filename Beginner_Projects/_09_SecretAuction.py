logo = r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

print(logo)

dic = {}


def bidder(bider , bid):
    dic[bider] = bid


while True:


    bider = input("\nEnter your name: ")
    bid = int(input("Enter your bid: $"))

    bidder(bider , bid)

    other = input("is there any other bidder? (y/n): ")

    if other.lower() == "n":
        max_key = max(dic, key = dic.get)
        print(f"\nWinner is {max_key} with bid of {dic[max_key]}")
        break

    elif other.lower() == "y":
        pass
    else:
        print("Invalid Input")





