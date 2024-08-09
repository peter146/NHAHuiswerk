weekmenu = {
    "maandag" : "spaghetti",
    "dinsdag" : "stoofvlees",
    "woensdag" : "ossobuco",
    "donderdag" : "chili con carne",
    "vrijdag" : "slibtong",
    "zaterdag" : "blinde vinken",
    "zondag" : "spinazie"}

dag = input("Voor welke dag van de week wil je graag het gerecht weten? ")

if dag in weekmenu:
    print("Op {dag} eten we {value}.".format(dag=dag, value=weekmenu[dag]))

else:
    print("Foute invoer, probeer opnieuw.")