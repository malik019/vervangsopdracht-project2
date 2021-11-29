from fietsen import Fietsen


class VeloSysteem(Fietsen):
    def __init__(self):
        self._velo_station = {
         1: Locatie("Antwerpen Central"),
         2: Locatie("Merksem"),
         3: Locatie("Holandstraat")
        }
        self._fietsen= {
            1: Fietsen(40, self.fietsers(1), self.transporteur(5)),
            2: Fietsen(30, self.fietsers(3), self.transporteur(4)),
            3: Fietsen(0, self.fietsers(4), self.transporteur(30)),
        }
        self._keuze = None
        self.plaats = None
        self.fiets = None


    def is_kies_location(self):
        print("Make een keuze (1-3)"
              "\n*******************"
              "\n1) Antwepren Central"
              "\n2) Merksem"
              "\n3) Holandstraat\n")
        self._keuze = input()
        self.plaats = self._velo_station.get(int(self._keuze))
        if not self.plaats:
            print("Invoer bestand niet")
        print(self.plaats)
        self.fiets = self._fietsen.get(int(self._keuze))
        print(self.fiets)

    def fietsers(self, aantal):
        return aantal

    def transporteur(self, fietsen):

        return fietsen





class Locatie(VeloSysteem):
    def __init__(self, plaats):
        self.plaats = plaats

    def __str__(self):
        return f'Dok station: {self.plaats}'



















