
class Fietsen():
    def __init__(self, aantal, fietsers, transport):
        self.aantal = aantal
        self.transport = transport
        self.fietseers = fietsers

    def __str__(self):
        return f'Beschikbare fietsen: {self.aantal}\nBeschiekbare fitsen {self.aantal + self.transport}\nBeschiekbare fitsen {self.aantal-self.fietseers}'










