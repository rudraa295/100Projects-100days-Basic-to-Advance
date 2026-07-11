def calculate_love_score(name1, name2):

    a = "TRUE"
    b = "LOVE"
    x = 0
    y = 0


    for char in a:
        x += name1.upper().count(char)
        x += name2.upper().count(char)

    for char in b:
        y += name1.upper().count(char)
        y += name2.upper().count(char)


    print(str(x)+str(y))


calculate_love_score(name1 = "Angela Yu"  , name2 = "Jack Bauer")
