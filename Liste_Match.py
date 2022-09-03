from tkinter import *
from LES_Classe import *

class ListeMatch(Tk):
    def __init__(self):
        super().__init__()
        self.title("Liste Match")
        self.geometry("350x330")
        self.Initialise()
        self.bind("<Map>", self.load())
    def load(self):
        Listematch=[]
        for match in Match.Liste_Matchs:
            Listematch.append(str(match))
        self.list.set(Listematch)

    def Initialise(self):
        self.list = StringVar(self)
        self.lbl=Label(self,text="La Liste des Match :").place(x=20,y=30)
        self.ListEquipe=Listbox(self,listvariable=self.list,width=50,height=15).place(x=20,y=50)