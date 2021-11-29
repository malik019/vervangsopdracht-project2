from velo_station import VeloSysteem
from contactgegevens import AdresLijst

class GebruikersDatabase:
    def __init__(self,):
        self._gebruikers = [
            {
                'id': 1,
                'naam': 'Joyce Wallace',
                'pas': 'week'
            },
            {
                'id': 2,
                'naam': 'Withney Kopers',
                'pas': 'dag'
            },
            {
                'id': 3,
                'naam': 'Joyce Wallace',
                'pas': 'geen'
            },
            {
                'id': 4,
                'naam': 'Kim Page',
                'pas': 'jaar'
            }
        ]


        self.velo_systeem = VeloSysteem()
        self.gebruiker_adressen = AdresLijst()

    def gebruikers(self):
        return [self._gebruiker_aanmaken(**data) for data in self._gebruikers]

    def _gebruiker_aanmaken(self, id, naam, pas):
        adres = self.gebruiker_adressen.geef_werknemer_adres(id)
        return Gebruiker(id, naam, adres, pas)

    def toon(self, gebruikers):
        print('Gebruikersgegevens')
        print('******************')
        for gebruiker in gebruikers:
            gebruiker.printen()

class Gebruiker():
    def __init__(self, id, naam, adres, pas):
        self.id = id
        self.naam = naam
        self.adres = adres
        self.pas = pas
        self.plaats = VeloSysteem().plaats
        self.fiets = VeloSysteem().fiets


    def printen(self):
        print(f'id: {self.id}\nnaam: {self.naam} \nadres: {self.adres}\npas: {self.pas}\nfiets-id: {self.plaats}{self.fiets}\n')














