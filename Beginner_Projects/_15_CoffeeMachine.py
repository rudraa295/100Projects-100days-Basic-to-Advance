import prettytable as pt
table = pt.PrettyTable()
table.add_column("Option",["1","2","3"])
table.align["Option"] = "l"
table.add_column("Type",["ESPRESSO","LATAE","CAPICHINO"])
table.align["Type"] = "l"
table.add_column("Price",[275,390,580])
print(table)

stock_igr = [1000,100,500]

def stock():
    print(f"""\n{stock_igr[0]}ml of water is left
{stock_igr[1]}gm of Coffee is left
{stock_igr[2]}ml of Milk is left""")

class Money:
    def __init__(self,money1,money2,inp):
        self.money1 = money1
        self.money2 = money2
        self.inp = inp

        if inp == "1":
            change = (money1*100)+(money2*500)-275

            if change == 0:
                print("\nPAYMENT SUCCESSFUL")
                print("WAIT ... Your ESPRESSO will be ready in 5 minutes")
            elif change < 0:
                print("\nPAYMENT UNSUCCESSFUL ... INSUFFICIENT MONEY")
                print(f"Your Rs{(money1*100)+(money2*500)} will be credited in 3 working days")
            elif change > 0:
                print(f'\nTake your change: {change}')
                print("PAYMENT SUCCESSFUL")
                print("WAIT ... Your ESPRESSO will be ready in 5 minutes")

        if inp == "2":
            change = (money1*100)+(money2*500)-390

            if change == 0:
                print("\nPAYMENT SUCCESSFUL")
                print("WAIT ... Your LATAE will be ready in 5 minutes")
            elif change < 0:
                print("\nPAYMENT UNSUCCESSFUL ... INSUFFICIENT MONEY")
                print(f"Your Rs{(money1*100)+(money2*500)} will be credited in 3 working days")
            elif change > 0:
                print(f'\nTake your change: {change}')
                print("PAYMENT SUCCESSFUL")
                print("WAIT ... Your LATAE will be ready in 5 minutes")

        if inp == "3":
            change = (money1*100)+(money2*500)-580

            if change == 0:
                print("\nPAYMENT SUCCESSFUL")
                print("WAIT ... Your CAPICHINO will be ready in 5 minutes")
            elif change < 0:
                print("\nPAYMENT UNSUCCESSFUL ... INSUFFICIENT MONEY")
                print(f"Your Rs{(money1*100)+(money2*500)} will be credited in 3 working days")
            elif change > 0:
                print(f'\nTake your change: {change}')
                print("PAYMENT SUCCESSFUL")
                print("WAIT ... Your CAPICHINO will be ready in 5 minutes")

        # return change

while True:

    inp = input("""\nWhat do you want :""").lower()

    if inp == 'stock':
        stock()

    elif inp == "1":
        print("""\nPay the bill :""")
        money1 = int(input("Rs100 note ? :"))
        money2 = int(input("Rs500 note ? :"))
        Money(money1,money2,inp)

    elif inp == "2":
        print("""\nPay the bill :""")
        money1 = int(input("Rs100 note ? :"))
        money2 = int(input("Rs500 note ? :"))
        Money(money1,money2,inp)

    elif inp == "3":
        print("""\nPay the bill :""")
        money1 = int(input("Rs100 note ? :"))
        money2 = int(input("Rs500 note ? :"))
        Money(money1,money2,inp)

    else:
        print("Wrong Option")
        continue

    fnl = input("\nAnything Else (y/n)? ")

    if fnl == "y":
        pass
    elif fnl == "n":
        # print(f"Your Change: {Money(money1,money2,inp)}")
        break













