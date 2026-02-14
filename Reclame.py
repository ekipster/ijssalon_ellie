from algemene_functies import Mijn_Functie_2
def Aanbieding_1():
    Mijn_dictionary = {
        "smaak" : "aardbei",
        "prijs" : 4,
        "korting" : 0.1}
    aanbieding = Mijn_dictionary["prijs"] - (Mijn_dictionary["prijs"] * Mijn_dictionary["korting"])
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Mijn_dictionary['smaak']}, van {Mijn_dictionary['prijs']} euro voor {aanbieding} euro.")
Aanbieding_1()

def Inkomsten_totaal():
    mijn_dictionary = {
        "Inkomsten" : [220, 430, 125, 160, 205, 90, 345],
        "BTW"  : 0.09}
    totaal = sum(mijn_dictionary["Inkomsten"])
    bedrag = totaal * mijn_dictionary["BTW"]

    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")
Inkomsten_totaal()

def Laag_en_hoog():
    mijn_lijst = {
        "fictieve inkomsten" : [220, 430, 125, 160, 205, 90, 345]}
    laagste = min(mijn_lijst["fictieve inkomsten"])
    hoogste = max(mijn_lijst["fictieve inkomsten"])

    print(f"het laagste inkomsten van deze week is {laagste} euro en jet hoogste inkomsten is {hoogste} euro.")
Laag_en_hoog()

def Gemiddelde():
    mijn_lijst = {
        "fictieve inkomsten" : [220, 430, 125, 160, 205, 90, 345]}
    gemiddelde = sum(mijn_lijst["fictieve inkomsten"]) / len(mijn_lijst["fictieve inkomsten"])

    print(f"De gemiddelde inkomsten van deze week zijn {gemiddelde} euro.")
Gemiddelde()

def Meervoudig():
    Laag_en_hoog()
    Invoer_lijst = {
        "getallen" : [10, 5, 3, 2, 1, 2, 9]}
    
    print(f"hoogste waarde: {max(Invoer_lijst['getallen'])}, laagste waarde: {min(Invoer_lijst['getallen'])}")
Meervoudig()

def combinatie(invoer_lijst_2):
    korte_lijst = Laag_en_hoog(invoer_lijst_2)
    uitvoer = Mijn_Functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer





