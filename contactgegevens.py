class AdresLijst:
    def __init__(self):
        self._werknemer_adressen = {
            1: Adres('Lange Leemstraat 34', 'Antwerpen', 2018, 'Bus 202'),
            2: Adres('Kloosterstraat 15', 'Antwerpen', 2000),
            3: Adres('Grote Markt 4', 'Antwerpen', 2000),
            4: Adres('Ellermanstraat 33', 'Antwerpen', 2060),
            5: Adres('Esmoreitlaan 7', 'Antwerpen', 2050)
        }

    def geef_werknemer_adres(self, werknemer_id):
        adres = self._werknemer_adressen.get(werknemer_id)
        if not adres:
            raise ValueError(werknemer_id)
        return adres

class Adres:
    def __init__(self, straat, stad, postcode, straat2=''):
        self.straat = straat
        self.straat2 = straat2
        self.stad = stad
        self.postcode = postcode

    def __str__(self):
        regels = [self.straat]
        if self.straat2:
            regels.append(self.straat2)
        regels.append(f'{self.postcode} {self.stad}')
        return '\n'.join(regels)