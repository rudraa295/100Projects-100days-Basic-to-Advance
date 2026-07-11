import random
from importlib.metadata import pass_none

print('''Press 1 for Stone
 Press 2 for Paper
  press 3 for Scissor''')

y = int(input("Enter Your Answer: "))

x = random.randint(1, 3)

print("Yours Rock" if y == 1 else "Yours Paper" if y == 2 else "Yours Scissor" if y == 3 else " wrong input" , end=" ")
print("Mine Rock" if x == 1 else "Mine Paper" if x == 2 else "Mine Scissor" if x == 3 else pass_none() )
if x == y:
    print("Tie")
elif (((x == 3) and (y == 1)) or ((x == 2) and (y == 3)) or ((x == 1) and (y == 2))):
    print("You Win")
elif (((x == 1) and (y == 3)) or ((x == 2) and (y == 1)) or ((y == 2) and (x == 3))):
    print("You Lose")
else:
    pass
