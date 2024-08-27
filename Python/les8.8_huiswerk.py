# create class
class CursistenRegister:
    def __init__(self, voornaam, achternaam, adres, email):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.adres = adres
        self.email = email

    def welkomstbericht(self):
        print("Welkom " + self.voornaam + " " + self.achternaam + ". Uw bestelling is verzonden naar " + self.adres + ". U krijgt een bevestiging op uw e-mailadres " + self.email + ".")

# create instance
cursist = CursistenRegister("Peter", "Rosa", "Picardielaan 56 in Schilde", "peter146@gmail.com")

# call method
cursist.welkomstbericht()
