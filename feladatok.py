from Stadion import Stadion
from datetime import datetime

def NYstadion(stadionok):
    NY_stadionok = 0
    for o in range(0,len(stadionok),1):
        if (stadionok[o].varos == "New York"):
            NY_stadionok += 1
    return NY_stadionok

def csapatszam(stadionok):
    csapatszam = 0
    for i in range(0,len(stadionok),1):
        csapatszam += stadionok[i].csapatokSZ
    return csapatszam

def elobb(stadionok):
    lista = []
    ido = datetime.strptime("1900-1-1", "%Y-%m-%d")
    for i in range(0,len(stadionok),1):
        if (stadionok[i].elso_merkozes < ido):
            lista.append(stadionok[i].nev)
    return lista

def ketezerota(stadionok):
    lista2 = []
    ido2 = datetime.strptime("2000-1-1", "%Y-%m-%d")
    for i in range(0,len(stadionok),1):
        if (stadionok[i].utolso_merkozes < ido2):
            lista2.append(stadionok[i].nev)
    return lista2

def buffalo(stadionok):
    osszes = 0
    for i in range(0,len(stadionok),1):
        if (stadionok[i].varos == "Buffalo"):
            osszes += stadionok[i].csapatokSZ
    return osszes