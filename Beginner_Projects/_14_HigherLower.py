import random

a = [
    {"name": 'Cristiano Ronaldo', "follower_count": 660, "description": 'Footballer', "country": 'Portugal'},
    {"name": 'Lionel Messi', "follower_count": 505, "description": 'Footballer', "country": 'Argentina'},
    {"name": 'Selena Gomez', "follower_count": 420, "description": 'Singer and actress', "country": 'United States'},
    {"name": 'Taylor Swift', "follower_count": 285, "description": 'Singer-songwriter', "country": 'United States'},
    {"name": 'Ariana Grande', "follower_count": 375, "description": 'Singer and actress', "country": 'United States'},
    {"name": 'Kylie Jenner', "follower_count": 395, "description": 'Media personality', "country": 'United States'},
    {"name": 'Kim Kardashian', "follower_count": 355, "description": 'Media personality', "country": 'United States'},
    {"name": 'Dwayne Johnson', "follower_count": 393, "description": 'Actor and former wrestler', "country": 'United States'},
    {"name": 'Virat Kohli', "follower_count": 275, "description": 'Cricketer', "country": 'India'},
    {"name": 'Neymar Jr.', "follower_count": 230, "description": 'Footballer', "country": 'Brazil'},
    {"name": 'Justin Bieber', "follower_count": 295, "description": 'Singer', "country": 'Canada'},
    {"name": 'Zendaya', "follower_count": 185, "description": 'Actress', "country": 'United States'},
    {"name": 'Billie Eilish', "follower_count": 125, "description": 'Singer', "country": 'United States'},
    {"name": 'Rihanna', "follower_count": 150, "description": 'Singer and entrepreneur', "country": 'Barbados'},
    {"name": 'Beyoncé', "follower_count": 320, "description": 'Singer', "country": 'United States'},
    {"name": 'Jennifer Lopez', "follower_count": 255, "description": 'Singer and actress', "country": 'United States'},
    {"name": 'Shakira', "follower_count": 95, "description": 'Singer', "country": 'Colombia'},
    {"name": 'Miley Cyrus', "follower_count": 210, "description": 'Singer', "country": 'United States'},
    {"name": 'Katy Perry', "follower_count": 205, "description": 'Singer', "country": 'United States'},
    {"name": 'Nicki Minaj', "follower_count": 230, "description": 'Rapper', "country": 'United States'},
    {"name": 'Dua Lipa', "follower_count": 90, "description": 'Singer', "country": 'United Kingdom'},
    {"name": 'Bruno Mars', "follower_count": 40, "description": 'Singer', "country": 'United States'},
    {"name": 'Ed Sheeran', "follower_count": 50, "description": 'Singer-songwriter', "country": 'United Kingdom'},
    {"name": 'Drake', "follower_count": 145, "description": 'Rapper', "country": 'Canada'},
    {"name": 'Eminem', "follower_count": 45, "description": 'Rapper', "country": 'United States'},
    {"name": 'Lady Gaga', "follower_count": 60, "description": 'Singer and actress', "country": 'United States'},
    {"name": 'Camila Cabello', "follower_count": 65, "description": 'Singer', "country": 'Cuba'},
    {"name": 'Shawn Mendes', "follower_count": 75, "description": 'Singer', "country": 'Canada'},
    {"name": 'Demi Lovato', "follower_count": 155, "description": 'Singer', "country": 'United States'},
    {"name": 'Chris Hemsworth', "follower_count": 60, "description": 'Actor', "country": 'Australia'},
    {"name": 'Tom Holland', "follower_count": 65, "description": 'Actor', "country": 'United Kingdom'},
    {"name": 'Robert Downey Jr.', "follower_count": 58, "description": 'Actor', "country": 'United States'},
    {"name": 'Chris Evans', "follower_count": 25, "description": 'Actor', "country": 'United States'},
    {"name": 'Keanu Reeves', "follower_count": 18, "description": 'Actor', "country": 'Canada'},
    {"name": 'Leonardo DiCaprio', "follower_count": 62, "description": 'Actor', "country": 'United States'},
    {"name": 'Johnny Depp', "follower_count": 32, "description": 'Actor', "country": 'United States'},
    {"name": 'Will Smith', "follower_count": 70, "description": 'Actor', "country": 'United States'},
    {"name": 'Tom Cruise', "follower_count": 15, "description": 'Actor', "country": 'United States'},
    {"name": 'Ryan Reynolds', "follower_count": 55, "description": 'Actor', "country": 'Canada'},
    {"name": 'Emma Watson', "follower_count": 75, "description": 'Actress', "country": 'United Kingdom'},
    {"name": 'Scarlett Johansson', "follower_count": 20, "description": 'Actress', "country": 'United States'},
    {"name": 'Gal Gadot', "follower_count": 110, "description": 'Actress', "country": 'Israel'},
    {"name": 'Margot Robbie', "follower_count": 32, "description": 'Actress', "country": 'Australia'},
    {"name": 'Millie Bobby Brown', "follower_count": 64, "description": 'Actress', "country": 'United Kingdom'},
    {"name": 'MrBeast', "follower_count": 70, "description": 'YouTuber', "country": 'United States'},
    {"name": 'PewDiePie', "follower_count": 20, "description": 'YouTuber', "country": 'Sweden'},
    {"name": 'Mark Rober', "follower_count": 10, "description": 'YouTuber', "country": 'United States'},
    {"name": 'KSI', "follower_count": 13, "description": 'YouTuber and musician', "country": 'United Kingdom'},
    {"name": 'Logan Paul', "follower_count": 28, "description": 'YouTuber', "country": 'United States'},
    {"name": 'Jake Paul', "follower_count": 28, "description": 'YouTuber', "country": 'United States'},
    {"name": 'Marques Brownlee', "follower_count": 5, "description": 'Tech YouTuber', "country": 'United States'},
    {"name": 'CarryMinati', "follower_count": 22, "description": 'YouTuber', "country": 'India'},
    {"name": 'Bhuvan Bam', "follower_count": 20, "description": 'YouTuber', "country": 'India'},
    {"name": 'Ashish Chanchlani', "follower_count": 18, "description": 'YouTuber', "country": 'India'},
    {"name": 'Technical Guruji', "follower_count": 7, "description": 'Tech YouTuber', "country": 'India'},
    {"name": 'Sandeep Maheshwari', "follower_count": 6, "description": 'Motivational speaker', "country": 'India'},
    {"name": 'Elon Musk', "follower_count": 8, "description": 'Entrepreneur', "country": 'United States'},
    {"name": 'Bill Gates', "follower_count": 12, "description": 'Entrepreneur', "country": 'United States'},
    {"name": 'Mark Zuckerberg', "follower_count": 14, "description": 'Entrepreneur', "country": 'United States'},
    {"name": 'Jeff Bezos', "follower_count": 5, "description": 'Entrepreneur', "country": 'United States'},
    {"name": 'Steve Harvey', "follower_count": 12, "description": 'Television host', "country": 'United States'},
    {"name": 'Gordon Ramsay', "follower_count": 18, "description": 'Chef', "country": 'United Kingdom'},
    {"name": 'Oprah Winfrey', "follower_count": 23, "description": 'Television host', "country": 'United States'},
    {"name": 'Barack Obama', "follower_count": 37, "description": 'Former president', "country": 'United States'},
    {"name": 'Narendra Modi', "follower_count": 92, "description": 'Prime Minister', "country": 'India'},
    {"name": 'Donald Trump', "follower_count": 33, "description": 'Politician', "country": 'United States'},
    {"name": 'NASA', "follower_count": 98, "description": 'Space agency', "country": 'United States'},
    {"name": 'SpaceX', "follower_count": 22, "description": 'Aerospace company', "country": 'United States'},
    {"name": 'National Geographic', "follower_count": 285, "description": 'Magazine', "country": 'United States'},
    {"name": 'Guinness World Records', "follower_count": 55, "description": 'Organization', "country": 'United Kingdom'},
    {"name": 'Netflix', "follower_count": 33, "description": 'Streaming platform', "country": 'United States'},
    {"name": 'Disney', "follower_count": 58, "description": 'Entertainment company', "country": 'United States'},
    {"name": 'Marvel', "follower_count": 70, "description": 'Entertainment company', "country": 'United States'},
    {"name": 'DC', "follower_count": 36, "description": 'Entertainment company', "country": 'United States'},
    {"name": 'PlayStation', "follower_count": 33, "description": 'Gaming brand', "country": 'Japan'},
    {"name": 'Xbox', "follower_count": 18, "description": 'Gaming brand', "country": 'United States'},
    {"name": 'Nintendo', "follower_count": 9, "description": 'Gaming company', "country": 'Japan'},
    {"name": 'Apple', "follower_count": 35, "description": 'Technology company', "country": 'United States'},
    {"name": 'Samsung', "follower_count": 20, "description": 'Technology company', "country": 'South Korea'},
    {"name": 'Google', "follower_count": 16, "description": 'Technology company', "country": 'United States'},
    {"name": 'Microsoft', "follower_count": 15, "description": 'Technology company', "country": 'United States'},
    {"name": 'Amazon', "follower_count": 8, "description": 'E-commerce company', "country": 'United States'},
    {"name": 'Tesla', "follower_count": 7, "description": 'Automotive company', "country": 'United States'},
    {"name": 'Adidas', "follower_count": 31, "description": 'Sportswear brand', "country": 'Germany'},
    {"name": 'Nike', "follower_count": 305, "description": 'Sportswear brand', "country": 'United States'},
    {"name": 'Puma', "follower_count": 14, "description": 'Sportswear brand', "country": 'Germany'},
    {"name": 'Ferrari', "follower_count": 31, "description": 'Automobile manufacturer', "country": 'Italy'},
    {"name": 'Lamborghini', "follower_count": 36, "description": 'Automobile manufacturer', "country": 'Italy'},
    {"name": 'Red Bull', "follower_count": 28, "description": 'Energy drink brand', "country": 'Austria'},
    {"name": 'FC Barcelona', "follower_count": 140, "description": 'Football club', "country": 'Spain'},
    {"name": 'Real Madrid', "follower_count": 180, "description": 'Football club', "country": 'Spain'},
    {"name": 'Manchester United', "follower_count": 65, "description": 'Football club', "country": 'England'},
    {"name": 'Manchester City', "follower_count": 55, "description": 'Football club', "country": 'England'},
    {"name": 'Paris Saint-Germain', "follower_count": 65, "description": 'Football club', "country": 'France'},
    {"name": 'FIFA', "follower_count": 52, "description": 'Sports organization', "country": 'Switzerland'},
    {"name": 'UEFA', "follower_count": 18, "description": 'Sports organization', "country": 'Switzerland'},
    {"name": 'Indian Premier League', "follower_count": 18, "description": 'Cricket league', "country": 'India'},
    {"name": 'Chennai Super Kings', "follower_count": 18, "description": 'Cricket team', "country": 'India'},
    {"name": 'Mumbai Indians', "follower_count": 17, "description": 'Cricket team', "country": 'India'},
    {"name": 'Royal Challengers Bengaluru', "follower_count": 20, "description": 'Cricket team', "country": 'India'},
]

logo = r"""
    __  ___      __               
   / / / (_)____/ /_  ___  ______ 
  / /_/ / / __  / __ \/ _ \/ ___/ 
 / __  / / /_/ / / / /  __/ /     
/_/ /_/_/\__, /_/ /_/\___/_/      
        /____/                    
    __                            
   / /   ____ _      _____  _____ 
  / /   / __ \ | /| / / _ \/ ___/ 
 / /___/ /_/ / |/ |/ /  __/ /     
/_____/\____/|__/|__/\___/_/      
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____/  
"""


def content():
    x = random.choice(a)
    a.remove(x)
    return x

v = True
d = {}
points = 0

while True:

    print(logo)

    if v == True:
        optA = content()
    else:
        optA = d

    print(f"\nOption A: {optA["name"]} , {optA['description']} from {optA['country']}")

    print(vs)

    optB = content()
    print(f"Option B: {optB["name"]} , {optB['description']} from {optB['country']} \n")


    inp = input("Enter any option (A/B): ").upper()

    if inp == "A":
        if optA["follower_count"] > optB["follower_count"]:
            points+=1
            v = False
            d = optA
        elif optA["follower_count"] < optB["follower_count"]:
            print(f"--- You Lose --- Points are {points}")
            break
        else:
            print("Equal")
            break

    elif inp == "B":
        if optB["follower_count"] > optA["follower_count"]:
            points += 1
            v = False
            d = optB
        elif optB["follower_count"] < optA["follower_count"]:
            print(f"--- You Lose --- Points are {points}")
            break
        else:
            print("Equal")
            break

    else:
        print("Wrong Input")


    if len(a) == 0:
        print(f"Congratulations ... You Win ... Your Score is {points}")
        break
    else:
        pass























