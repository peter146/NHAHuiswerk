"""Schrijf een code die aan de gebruiker een getal vraagt. Als het getal hoger is dan 50, dan dient de code een tekstbestand aan te maken met daarin een zelfgekozen boodschap. Stuur het py-bestand naar uw docent."""

import sys

def main():
    input_correct = False
    while not input_correct:
        try:
            getal = int(input("Voer een getal in tussen 0 en 100: "))
            if 0 <= getal <= 100: # getal tussen 0 en 100?
                if getal > 50: # getal groter dan 50?
                    input_correct = True
                    boodschap = input("Correct! Voer nu een persoonlijke boodschap in: ")
                    with open("test.txt", mode = "wt", encoding="utf-8") as f:
                        f.writelines(boodschap)
                    print("Boodschap correct opgeslagen in test.txt")
                else:
                    print("Getal moet hoger zijn dan 50")
            else:
                print("Foute input: getal moet tussen 0 en 100 liggen")
        except ValueError: 
            print("Fout input: voer een geldig getal in")
        except Exception as e:
            print("Er ging iets mis: {e}")

main()