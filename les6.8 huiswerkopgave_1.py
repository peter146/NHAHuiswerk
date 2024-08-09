weekmenu = {
    "maandag": "spaghetti",
    "dinsdag": "stoofvlees",
    "woensdag": "ossobuco",
    "donderdag": "chili con carne",
    "vrijdag": "slibtong",
    "zaterdag": "blinde vinken",
    "zondag": "spinazie"
}

dag = input("Geef een weekdag op: ")

try:
    if dag in weekmenu:
        print(f"Op {dag} eten we {weekmenu[dag]}.")
    else:
        raise ValueError("Ongeldige weekdag ingevoerd, probeer opnieuw.")
except ValueError as e:
    print(e)
finally:
    print("Einde module")
