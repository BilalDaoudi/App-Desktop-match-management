from tkinter import *
from LES_Classe import *
from tkinter import messagebox
class Find_Arbitre(Tk):
    def __init__(self):
        super().__init__()
        self.title("Rechercher Arbitre")
        self.geometry("300x250")
        self.Initialise()

    def Initialise(self):
        self.lbl2 = Label(self, text="CIN :").place(x=20, y=20)
        self.lbl3 = Label(self, text="Nom :").place(x=20, y=50)
        self.lbl4 = Label(self, text="Prénom :").place(x=20, y=80)
        self.lbl5 = Label(self, text="Date Naissance :").place(x=20, y=110)
        self.lbl6 = Label(self, text="Nationalité :").place(x=20, y=140)
        self.lbl7 = Label(self, text="Position :").place(x=20, y=170)

        self.VarCIN = StringVar(self)
        self.VarNom = StringVar(self)
        self.VarPrenom = StringVar(self)
        self.VarDt = StringVar(self)
        self.VarPosition = StringVar(self)
        self.VarNation = StringVar(self)

        self.entCIN = Entry(self,textvariable=self.VarCIN).place(x=120, y=20)
        self.entNom = Entry(self,textvariable=self.VarNom).place(x=120, y=50)
        self.entPrenom = Entry(self,textvariable=self.VarPrenom).place(x=120, y=80)
        self.entDt = Entry(self,textvariable=self.VarDt).place(x=120, y=110)
        self.entPosition = Entry(self,textvariable=self.VarPosition).place(x=120, y=140)
        self.entNation = Entry(self,textvariable=self.VarNation).place(x=120, y=170)


        self.btnRechercher=Button(self,text="Rechercher Arbitre",command=self.Rechercher_Arbitre)
        self.btnRechercher.place(x=90,y=210)

    def Rechercher_Arbitre(self):
        cin=self.VarCIN.get()
        if cin != "":
            arb=Arbire.Find_Arbire(cin)
            if arb != None:
                self.VarNom.set(arb.Nom)
                self.VarPrenom.set(arb.Prenom)
                self.VarDt.set(arb.DateNaissance)
                self.VarNation.set(arb.Nationalite)
                self.VarPosition.set(arb.Position)
            else:
                messagebox.showinfo("Recherche Arbitre","Arbitre n'est pas existe !!!")
        else:
            messagebox.showerror("Mauvaise Saisir","Donner CIN de Arbitre à Rechercher")




