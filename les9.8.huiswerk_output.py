"""Schrijf een code die de boodschap toont uit het tekstbestand van de vorige opgage. Stuur het py-bestand naar uw docent."""

def open_bestand():
    try:
        with open("test.txt", mode="rt", encoding="utf-8") as file:
            content = file.read()
            print("Deze tekst werd teruggevonden in test.txt: \n")
            print("\t", "'", content, "'")
    except FileNotFoundError:
        print("Bestand niet gevonden")
    except Exception as e:
        print("Er ging iets mis: {e}")

open_bestand()