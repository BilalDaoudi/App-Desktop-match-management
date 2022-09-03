from tkinter import *
from LES_Classe import *
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import Combobox
class Update_Equipe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Modifier Equipe")
        self.geometry("400x330")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.list = []
        for equi in Equipe.T_Equipe:
            self.list.append(equi.Nom)
        self.CmpNomEqui["values"] = self.list
    def Initialise(self):
        self.lbl=Label(self,text="Equipe Modifier :").place(x=20,y=20)
        self.CmpNomEqui = Combobox(self)
        self.CmpNomEqui.place(x=120, y=20)
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
        self.lbl1 = Label(self, text="Nom Equipe :").place(x=20,y=50)
        self.lbl2 = Label(self, text="Date Création :").place(x=20, y=80)
        self.lbl3 = Label(self, text="Ville :").place(x=20, y=110)
        self.lbl4 = Label(self, text="Entrîneur :").place(x=20, y=130)
        self.lbl5 = Label(self, text="CIN Entrîneur :").place(x=50, y=160)
        self.lbl6 = Label(self, text="Nom Entrîneur :").place(x=50, y=185)
        self.lbl7 = Label(self, text="Prenom Entrîneur :").place(x=50, y=210)
        self.lbl8 = Label(self, text="Date Naissance :").place(x=50, y=230)
        self.lbl9 = Label(self, text="Nationalité :").place(x=50, y=255)
        # Les Entry
        self.entnomeq=Entry(self,textvariable=self.NomEq)
        self.entnomeq.place(x=120,y=50)
        self.entdtCrea = Entry(self, textvariable=self.DateCreation)
        self.entdtCrea.place(x=120, y=80)
        self.entville = Entry(self, textvariable=self.Ville)
        self.entville.place(x=120, y=110)
        self.entcin = Entry(self, textvariable=self.CinEntr)
        self.entcin.place(x=150, y=160)
        self.entnomentr = Entry(self, textvariable=self.NomEntr)
        self.entnomentr.place(x=150, y=185)
        self.entprentr = Entry(self, textvariable=self.PrenomEntr)
        self.entprentr.place(x=150, y=210)
        self.entdtentr = Entry(self, textvariable=self.DateNais)
        self.entdtentr.place(x=150, y=230)
        self.entnation = Entry(self, textvariable=self.Nationalite)
        self.entnation.place(x=150, y=255)
        # Les Button
        self.bntAjouter=Button(self,text="Modifier Equipe",command=self.Modifier_Equipe)
        self.bntAjouter.place(x=150,y=290)
        self.bntVider = Button(self, text="vider", command=self.Vider_Click)
        self.bntVider.place(x=260, y=290)

    def Vider_Click(self):
        self.NomEq.set("")
        self.DateCreation.set("")
        self.Ville.set("")
        self.CinEntr.set("")
        self.NomEntr.set("")
        self.PrenomEntr.set("")
        self.DateNais.set("")
        self.Nationalite.set("")
        self.CmpNomEqui.set("")
    def Modifier_Equipe(self):
        if self.CmpNomEqui.get() in self.list:
            b=True
            try:
                Dat = self.DateCreation.get()
                self.Dat=(datetime.strptime(Dat, "%d/%m/%Y")).date()
                dat = self.DateNais.get()
                self.datnais=(datetime.strptime(dat, "%d/%m/%Y")).date()

            except ValueError:
                messagebox.showerror("Mauvaise Saisir", "Donner La date a forme (jj/mm/aaaa)!!!!")
                b=False
            if b:
                equipe = Equipe.Find_Equipe(self.CmpNomEqui.get())
                equipe.Nom = self.NomEq.get()
                equipe.DateCreation = self.Dat
                equipe.Ville = self.Ville.get()
                equipe.Entraineur.CIN = self.CinEntr.get()
                equipe.Entraineur.Nom = self.NomEntr.get()
                equipe.Entraineur.Prenom = self.PrenomEntr.get()
                equipe.Entraineur.DateNaissance =self.datnais
                equipe.Entraineur.Nationalite = self.Nationalite.get()
                messagebox.showinfo("Modifier Equipe", "Equipe a Modifié")
        else:
            messagebox.showerror("Mauvaise Saisir","Choisir Nom Equipe")



