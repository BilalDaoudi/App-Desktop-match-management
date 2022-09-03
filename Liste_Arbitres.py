from tkinter import *
from LES_Classe import *

class Liste_Arbitres(Tk):
    def __init__(self):
        super().__init__()
        self.title("Liste Arbitres")
        self.geometry("540x330")
        self.bind("<Map>",self.load())
        self.Initialise()
    def load(self):
        self.list=StringVar(self)
        self.list.set(Arbire.T_Arbitres)

    def Initialise(self):
        self.lbl=Label(self,text="La Liste des Arbitres :").place(x=20,y=30)
        self.ListEquipe=Listbox(self,listvariable=self.list,width=85,height=15).place(x=20,y=50)