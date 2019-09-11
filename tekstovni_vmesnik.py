import model

def izpis_stanja(potovanje):
    return """==========================
Stroški na osebo: {stroski_na_osebo}
{potnik1} plačal: {stanje1}
{potnik2} plačal: {stanje2}

==========================""".format(stroski_na_osebo = potovanje.stroski_na_osebo(),
potnik1=potovanje.potnika(potnik1), potnik2=potovanje.potnika(potnik2),
stanje1=potovanje.stanje(stanje1), stanje2=potovanje.stanje(stanje2))

def izpis_konca_potovanja(potovanje):
    return konec_potovanja()

def vnos_stroskov_prvega_potnika():
    return input("Prvi je plačal: ")

def vnos_stroskov_prvega_potnika():
    return input("Drugi je plačal: ")

def pozeni_vmesnik():
    potovanje = potovanje.novo_potovanje()
    while True:
        print(izpis_stanja(potovanje(igra))
        placal1 = vnos_stroskov_prvega_potnika()
        placal2 = vnos_stroskov_drugega_potnika()
        stanje1 += placal1
        stanje2 += placal2
        stroski_na_osebo += (placal1 + placal2) / 2
        
pozeni_vmesnik()