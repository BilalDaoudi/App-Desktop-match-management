from tkinter import *
from tkinter import messagebox
from LES_Classe import *
class Find_Equipe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Recherche Equipe")
        self.geometry("400x330")
        self.Initialise()
    def Initialise(self):
        # Les Variables
        self.NomEq = StringVar(self)
        self.DateCreation = StringVar(self)
        self.Ville = StringVar(self)
        self.CinEntr = StringVar(self)
        self.NomEntr = StringVar(self)
        self.PrenomEntr = StringVar(self)
        self.DateNais = StringVar(self)
        self.Nationalite = StringVar(self)
        # Les Label
        self.lbl1 = Label(self, text="Nom Equipe :").place(x=20,y=20)
        self.lbl2 = Label(self, text="Date Création :").place(x=20, y=50)
        self.lbl3 = Label(self, text="Ville :").place(x=20, y=80)
        self.lbl4 = Label(self, text="Entrîneur :").place(x=20, y=110)
        self.lbl5 = Label(self, text="CIN Entrîneur :").place(x=50, y=130)
        self.lbl6 = Label(self, text="Nom Entrîneur :").place(x=50, y=155)
        self.lbl7 = Label(self, text="Prenom Entrîneur :").place(x=50, y=180)
        self.lbl8 = Label(self, text="Date Naissance :").place(x=50, y=205)
        self.lbl9 = Label(self, text="Nationalité :").place(x=50, y=230)
        # Les Entry
        self.entnomeq=Entry(self,textvariable=self.NomEq)
        self.entnomeq.place(x=120,y=20)
        self.entdtCrea = Entry(self, textvariable=self.DateCreation)
        self.entdtCrea.place(x=120, y=50)
        self.entville = Entry(self, textvariable=self.Ville)
        self.entville.place(x=120, y=80)
        self.entcin = Entry(self, textvariable=self.CinEntr)
        self.entcin.place(x=150, y=130)
        self.entnomentr = Entry(self, textvariable=self.NomEntr)
        self.entnomentr.place(x=150, y=155)
        self.entprentr = Entry(self, textvariable=self.PrenomEntr)
        self.entprentr.place(x=150, y=180)
        self.entdtentr = Entry(self, textvariable=self.DateNais)
        self.entdtentr.place(x=150, y=205)
        self.entnation = Entry(self, textvariable=self.Nationalite)
        self.entnation.place(x=150, y=230)
        # Les Button
        self.bntAjouter=Button(self,text="Recherche Equipe",command=self.Recherche_Equipe)
        self.bntAjouter.place(x=150,y=280)

    def Recherche_Equipe(self):
        if self.NomEq.get()=="":
            messagebox.showerror("Mauvaise Saisir","Donner le nom de Equipe à Rechercher")
        else:
            nom=self.NomEq.get()
            test=Equipe.Find_Equipe(nom)
            if test==None:
                messagebox.showinfo("Recherche Equipe","Equipe n'est pas Existe")
            else:
                self.DateCreation.set(test.DateCreation)
                self.Ville.set(test.Ville)
                self.CinEntr.set(test.Entraineur.CIN)
                self.NomEntr.set(test.Entraineur.Nom)
                self.PrenomEntr.set(test.Entraineur.Prenom)
                self.DateNais.set(test.Entraineur.DateNaissance)
                self.Nationalite.set(test.Entraineur.Nationalite)


