x = float(input("What's the total bill amount?"))
y = float(input("How much tip would you like to give in percent?"))
z = float(input('How many people are sharing the table?'))

print(f"each person should give {((x*(y/100))+x)/z:.2f}")
