Mijn_dictionary = {"aardbei" : 3,
                   "Vanille" : 4,
                   "chocolade" : 5}
Aanbieding = Mijn_dictionary["aardbei"] * 0.8
Reclame_tekst = (f"vandaag in de aanbieding: Vanille-ijs, 1 liter - slechts €{Aanbieding}")
Reclame_tekst2 = Reclame_tekst[:62]
Reclame_tekst3 = Reclame_tekst2.upper()
Reclame_tekst4 = Reclame_tekst3.split()
el = Reclame_tekst4
for el in Reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())
        
    





