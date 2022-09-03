from tkinter import *

from LES_Classe import *

class ListeEquipe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Liste Equipe")
        self.geometry("540x330")
        self.bind("<Map>",self.load())
        self.Initialise()
    def load(self):
        self.list=StringVar(self)
        self.list.set(Equipe.T_Equipe)

    def Initialise(self):
        self.lbl=Label(self,text="La Liste des Equipes :").place(x=20,y=30)
        self.ListEquipe=Listbox(self,listvariable=self.list,width=85,height=15).place(x=20,y=50)