from tkinter import *
from LES_Classe import *
from tkinter.ttk import Combobox
from tkinter import messagebox

class Liste_Joueur(Tk):
    def __init__(self):
        super().__init__()
        self.title("Liste Joueurs")
        self.geometry("440x330")
        self.Initialise()
        self.bind("<Map>", self.load())

    def load(self):
        ListNomEq=[]
        for EQ in Equipe.T_Equipe:
            ListNomEq.append(EQ.Nom)
        self.ComNomEquipe["values"]=ListNomEq


    def Initialise(self):
        self.lbl1=Label(self,text="Nom Equipe :").place(x=20,y=20)
        self.ComNomEquipe=Combobox(self)
        self.ComNomEquipe.place(x=130,y=20)

        self.ListJou=StringVar(self)
        self.lbl2=Label(self,text="La Liste des Equipes :").place(x=20,y=50)
        self.ListEquipe=Listbox(self,listvariable=self.ListJou,width=65,height=12).place(x=20,y=70)

        self.bntListe=Button(self,text="Liste Joueur",command=self.Liste_Joueurs)
        self.bntListe.place(x=150,y=290)

    def Liste_Joueurs(self):
        if not(self.ComNomEquipe.get() == ""):
            nom = self.ComNomEquipe.get()
            equipe=Equipe.Find_Equipe(nom)
            self.ListJou.set(equipe.ListJoueurPrin)
        else:
            messagebox.showerror("Mauvaise Saisir","Donner Le Nom Equipe !!!!!!!!")

