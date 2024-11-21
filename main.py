from Stadion import Stadion
import fajlbeolvasas
import feladatok

stadionok = fajlbeolvasas.beolvas("stadionok.txt")

newyork = int(feladatok.NYstadion(stadionok))
csapatszam = feladatok.csapatszam(stadionok)
elotte = feladatok.elobb(stadionok)
ketezer = feladatok.ketezerota(stadionok)
buffalo = feladatok.buffalo(stadionok)

print("")
print(f"New Yorkban {newyork} db stadion van\n")
print(f"A csapatok száma: {csapatszam} db\n")
print(f"Stadionok amiknek 1900 volt az első meccse: {elotte}\n({len(elotte)}db összesen)\n")
print(f"Stadionok amiket 2000 óta nem használnak: {ketezer}\n({len(ketezer)}db összesen)\n")
print(f"A Buffaloban valaha játszó csapatok száma: {buffalo}\n")