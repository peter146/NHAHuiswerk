#!/usr/bin/env python3

# variabelen functie 1
welkom = "Welkom in dit nieuwe programma"
deelnemers = 5
scores = [3, 4, 2, 1, 5]

# functie 1
def print_info(x):
    print(x)
    print("type = ",type(x))
    print("id = ", id(x))
    print("len = ", len(str((x))))
    print()

#functie 2
def print_talen(naam, aantal, talen):
    print(f"Mijn naam is {naam}, en ik spreek {aantal} talen, namelijk {talen}")
    

# uitvoering functie 1
print_info(welkom)
print_info(deelnemers)
print_info(scores)

#uitvoering functie 2
print_talen("Peter", 4, "Nederlands, Frans, Duits en Engels")
