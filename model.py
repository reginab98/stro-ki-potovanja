import json

class Potovanje:

    def __init__(self, potnik1, potnik2, stanje1, stanje2):
        self.potnik1 = ""
        self.potnik2 = ""
        self.stanje1 = 0
        self.stanje2 = 0

    def novo_potovanje(self):
        self.stanje1 = 0
        self.stanje2 = 0

    def potnika(self, potnik1, potnik2): # Vpišemo dve imeni.
        self.potnik1 = input('Potnik 1: ')
        self.potnik2 = input('Potnik 2: ')

    def placilo1(self, placal1):
        self.stanje1 += placal1

    def placilo2(self, placal2):
        self.stanje2 += placal2

    def stroski_na_osebo(self):
        stroski_na_osebo = (self.stanje1 + self.stanje2) / 2
        return stroski_na_osebo
    

    def nasvet(self):
        if self.stanje1 > self.stanje2:
            return 'Naslednjič naj plača {}'.format(self.potnik2)
        elif  self.stanje2 > self.stanje1:
            return 'Naslednjič naj plača {}'.format(self.potnik1)
        else:
            return 'Vseeno je, kdo nasledjič plača.'

    def konec_potovanja(self): #gumb Konec potovanja. Ko kliknemo ta gumb, se izpiše, kdo naj komu koliko vrne.
        if self.stanje1 > self.stanje2:
            return '{0} mora {1} plačati {2} evrov.'.format(self.potnik2, self.potnik1, (self.stanje1 - self.stanje2) / 2 )
        elif self.stanje2 > self.stanje1:
            return '{0} mora {1} plačati {2} evrov.'.format(self.potnik1, self.potnik2, (self.stanje2 - self.stanje1) / 2 )
        else:
            return 'Nihče ni nikomur nič dolžan.'

    




         


    

