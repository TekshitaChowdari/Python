def build_profile(**details):
    print("PROFILE CARD")

    for key, value in details.items():
        print(key.upper(), ":", value)


build_profile(name="Tekshita", age=18, city="Rajam", hobby="Dancing")

build_profile(name="Rahul", age=20, city="Vizag")

build_profile(name="Priya", hobby="Reading", course="CSE")
#output:-
#PROFILE CARD
#NAME : Tekshita
#AGE : 18
#CITY : Rajam
#HOBBY : Dancing
#PROFILE CARD
#NAME : Rahul
#AGE : 20
#CITY : Vizag
#PROFILE CARD
#NAME : Priya
#HOBBY : Reading
#COURSE : CSE
