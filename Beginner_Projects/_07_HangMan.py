logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                     
                    |___/                      
'''



stages = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]


import random

print(logo)

words = ["Hello" , "World" , "Cruel"]

x = random.choice(words).lower()
print(x)


Blank = ["_"] * len(x)
stage = 0



while True:

    print(stages[stage])
    print(f"You have {6-stage} out of 6 lifes left\n")

    print(" ".join(Blank))

    if stage == 6:
        print("You Lose!")
        break

    c = input("Enter a char: ").lower()

    found = False

    for i in range(len(x)):
        if c == x[i]:
            Blank[i] = c
            found = True

    if found:
        print("Correct")
    else:
        print("Incorrect")
        stage += 1

    if "_" not in Blank:
        print(" ".join(Blank))
        print("🎉 You Win!")
        break

















