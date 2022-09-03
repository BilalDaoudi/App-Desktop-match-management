from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
class Find_Joueur(Tk):
    def __init__(self):
        super().__init__()
        self.title("Rechercher Joueur")
        self.geometry("460x210")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.list = []
        for equi in Equipe.T_Equipe:
            self.list.append(equi.Nom)
        self.CMPNomEq["values"] = self.list

    def Initialise(self):
        self.lbl1 = Label(self,text="Equipe :").place(x=20,y=20)
        self.lbl2 = Label(self, text="CIN :").place(x=240, y=20)
        self.lbl3 = Label(self, text="Nom :").place(x=60, y=60)
        self.lbl4 = Label(self, text="Prénom :").place(x=200, y=60)
        self.lbl5 = Label(self, text="Date Naissance :").place(x=320, y=60)
        self.lbl6 = Label(self, text="Numéro :").place(x=55, y=120)
        self.lbl7 = Label(self, text="Poste :").place(x=200, y=120)
        self.lbl8 = Label(self, text="Nationalité :").place(x=330, y=120)

        self.VarCIN = StringVar(self)
        self.VarNom = StringVar(self)
        self.VarPrenom = StringVar(self)
        self.VarDt = StringVar(self)
        self.VarNum = StringVar(self)
        self.VarPoste = StringVar(self)
        self.VarNation = StringVar(self)

        self.entCIN = Entry(self,textvariable=self.VarCIN).place(x=300, y=20)
        self.entNom = Entry(self,textvariable=self.VarNom).place(x=20, y=80)
        self.entPrenom = Entry(self,textvariable=self.VarPrenom).place(x=160, y=80)
        self.entDt = Entry(self,textvariable=self.VarDt).place(x=300, y=80)
        self.entNum = Entry(self,textvariable=self.VarNum).place(x=20, y=140)
        self.entPoste = Entry(self,textvariable=self.VarPoste).place(x=160, y=140)
        self.entNation = Entry(self,textvariable=self.VarNation).place(x=300, y=140)

        self.CMPNomEq=Combobox(self)
        self.CMPNomEq.place(x=75, y=20)

        self.btnRechercher=Button(self,text="Rechercher Joueur",command=self.Rechercher_Joueur)
        self.btnRechercher.place(x=170,y=170)

    def Rechercher_Joueur(self):
        nom=self.CMPNomEq.get()
        cin=self.VarCIN.get()
        if nom in self.list and cin != "":
            equipe=Equipe.Find_Equipe(nom)
            indice=equipe.Find_Joueur_Prin(cin)
            if indice != -1:
                J=equipe.ListJoueurPrin[indice]
                self.VarNom.set(J.Nom)
                self.VarPrenom.set(J.Prenom)
                self.VarDt.set(J.DateNaissance)
                self.VarNum.set(str(J.Numero))
                self.VarPoste.set(J.Poste)
                self.VarNation.set(J.Nationalite)
            else:
                self.VarNom.set("Null")
                self.VarPrenom.set("Null")
                self.VarDt.set("Null")
                self.VarNum.set("Null")
                self.VarPoste.set("Null")
                self.VarNation.set("Null")
                messagebox.showinfo("Rechercher Joueur",f"Joueur n'est pas Existe dans Equipe {nom}")
        else:
            messagebox.showerror("Mauvaise Saisir", "Donner Le Nom Equipe Et CIN Joueur")













