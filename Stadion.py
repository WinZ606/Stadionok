from datetime import datetime
class Stadion:
    def __init__(self,nev:str="",varos:str="",csapatokSZ:int=0,elso_merkozes:str="",utolso_merkozes:str=""):
        self.nev = nev
        self.varos = varos
        self.csapatokSZ = int(csapatokSZ)
        self.elso_merkozes = datetime.strptime(elso_merkozes, "%Y-%m-%d")
        self.utolso_merkozes = datetime.strptime(utolso_merkozes, "%Y-%m-%d")
        
    def __str__(self):
        return (f"Stadion neve: {self.nev}\n"
                f"Város: {self.varos}\n"
                f"Csapatok száma: {self.csapatokSZ}\n"
                f"Első mérkőzés: {self.elso_merkozes}\n"
                f"Utolsó mérkőzés: {self.utolso_merkozes}\n")