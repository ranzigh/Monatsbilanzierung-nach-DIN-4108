import Monatsbilanzierung



dach = Bilanz_5.Dach(name="Dach1", fläche=20)
wand1 = Bilanz_5.Außenwand("Wand1", 50,0)
wand2 = Bilanz_5.Außenwand("Wand2", 50,90)
wand3 = Bilanz_5.Außenwand("Wand3", 50,180)
wand4 = Bilanz_5.Außenwand("Wand4", 50,270)
fst1 = Bilanz_5.Fenster("Fenster1", 5, 0)
fst2 = Bilanz_5.Fenster("Fenster2", 7, 90)
fst3 = Bilanz_5.Fenster("Fenster3", 9, 180)
fst4 = Bilanz_5.Fenster("Fenster4", 11, 270)
fst5 = Bilanz_5.Fenster("Fenster5", 11, 270)
bpl = Bilanz_5.Bodenplatte("Bpl1", 20)

Testprojekt = Bilanz_5.Monatsbilanz(wand1,wand2,wand3,wand4, dach, bpl, fst1,fst2,fst3,fst4,fst5,
	name="Testprojekt", geschossanzahl=2, geschosshöhe=2.9, wärmebrückenzuschlag=0.05, 
	luftwechsel=0.6, einfamilienhaus=False, schweresGebäude=True)


Luftdichte, Innentemperatur, CwirkLuft, volumen, Cwirk, luftvolumen, nutzfläche, Hv = Testprojekt.konstanten_berechnen(bpl.fläche)
bauteilliste, hüllfläche, a_v_verhältnis = Testprojekt.bauteilliste_erstellen()
fensterliste = Testprojekt.fensterliste_erstellen()
monatsbilanzierung = Testprojekt.monatsbilanzierung_erstellen()

print(bauteilliste)

print(fensterliste)

print(monatsbilanzierung)


print ("Hüllfläche = ", hüllfläche)
#print ("Volumen = ", volumen)
#print ("Beh. Luftvolumen = ", luftvolumen)
#print ("Gebäudenutzfläche = ", nutzfläche)
#print ("A/V-Verhältnis = ", round(hüllfläche/volumen, 3))
print ("Fensterfläche = ", Testprojekt.fensterliste_erstellen()["Fläche"].sum())
print ("Fensterflächenanteil an Hüllfläche = ", round(Testprojekt.fensterliste_erstellen()["Fläche"].sum()/hüllfläche,3), "\n")



    # Ergebnisse
print ("Jahres-Heizwärmebedarf: ", monatsbilanzierung.loc["Heizwärmebedarf"].sum())
#print ("Flächenbezogener Jahres-Heizwärmebedarf: ", monatsbilanzierung.loc["Heizwärmebedarf"].sum()/nutzfläche)
#print ("Volumenbezogener Jahres-Heizwärmebedarf: ", monatsbilanzierung.loc["Heizwärmebedarf"].sum()/volumen)
#print ("Zahl der Heiztage: ", monatsbilanzierung.loc["Heiztage"].sum())
#print ("Heizgradtagzahl: ", heizgradtagzahl)
print ("Spezifischer Transmissionswärmeverlust: ", ((bauteilliste["W/K"].sum()+Testprojekt.wärmebrückenzuschlag*hüllfläche)/hüllfläche))
