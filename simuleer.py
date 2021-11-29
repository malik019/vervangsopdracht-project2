from velo_station import VeloSysteem
from gebruiker import GebruikersDatabase
from fietsen import Fietsen

oVelosysteem = VeloSysteem()
oGebruikersdatabse = GebruikersDatabase()

kies_locatie = oVelosysteem.is_kies_location()
fietsers= oVelosysteem.fietsers(2)
transport = oVelosysteem.transporteur(10)

gebruikers = oGebruikersdatabse.gebruikers()
toongebruiker = oGebruikersdatabse.toon(gebruikers)






