#!/usr/bin/env python3

naam = input("Hallo daar, hoe heet je? ") #naam wordt als parameter gebruikt in onderstaande functie

def aanspreking(naam):
    """Dit is een functie."""
    print("Dag " + str(naam) + ", ik ben Peter en heb voor jou deze module gemaakt.")

aanspreking(naam)
