logo = r'''
 ,adPPYba,  ,adPPYYba,  ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8 88P'   
8b          ,adPPPPP88  8PP"""""""   `"Y8ba,  ,adPPPPP88  88       
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I 88,    ,88  88       
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"' `"8bbdP"Y8  88       

'''


alphabet = [
    'a', 'b', 'c', 'd', 'e' , 'f', 'g',
    'h', 'i', 'j', 'k', 'l' , 'm', 'n',
    'o', 'p', 'q', 'r', 's' , 't', 'u',
    'v', 'w', 'x', 'y', 'z' , 'a', 'b',
    'c', 'd', 'e', 'f', 'g' , 'h', 'i',
    'j', 'k', 'l', 'm', 'n' , 'o', 'p',
    'q', 'r', 's', 't', 'u' , 'v', 'w',
    'x', 'y', 'z'
]



def encrypt(orignal , shift):

    encrypted = []

    for i in range(len(orignal)):

        if orignal[i] in alphabet:
            a = alphabet.index(orignal[i])
            encrypted.append(alphabet[a+shift])

        else:
            encrypted.append(orignal[i])

    return ''.join(encrypted)



def decrypt(orignald , shiftd):

    decrypted = []

    for i in range(len(orignald)):

        if orignald[i] in alphabet:
            a = alphabet.index(orignald[i])+26
            decrypted.append(alphabet[a-shiftd])

        else:
            decrypted.append(orignald[i])

    return ''.join(decrypted)


print("\n",logo)

while True:

    x = input("""\ne for encryption
    d for decryption
        x for exit program
= """)

    if x.lower() == "e":
        orignal = input("Enter the message to be encrypted: ").lower()
        shift = int(input("Enter the shift number: "))
        print(encrypt(orignal , shift))

    elif x.lower() == "d":
        orignald = input("Enter the message to be decrypted: ").lower()
        shiftd = int(input("Enter the shift number: "))
        print(decrypt(orignald , shiftd))

    elif x.lower() == "x":
        break

    else:
        print("Please enter a valid input")







