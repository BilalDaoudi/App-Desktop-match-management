from tkinter import *
from LES_Classe import *
from datetime import datetime
from tkinter import messagebox
class Add_Equipe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ajouter Equipe")
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
        self.bntAjouter=Button(self,text="Ajouter Equipe",command=self.Add_Click)
        self.bntAjouter.place(x=120,y=280)
        self.bntVider = Button(self, text="vider",command=self.Vider_Click)
        self.bntVider.place(x=210, y=280)

    def Vider_Click(self):
        self.NomEq.set("")
        self.DateCreation.set("")
        self.Ville.set("")
        self.CinEntr.set("")
        self.NomEntr.set("")
        self.PrenomEntr.set("")
        self.DateNais .set("")
        self.Nationalite.set("")
    def Add_Click(self):
        nomEq=self.NomEq.get()
        DtCrea=self.DateCreation.get()
        ville=self.Ville.get()
        cin=self.CinEntr.get()
        nomEntra=self.NomEntr.get()
        prenoEntra=self.PrenomEntr.get()
        DtNaiss=self.DateNais .get()
        nation=self.Nationalite.get()
        if (nomEq != "" and DtCrea != "" and ville != "" and cin != "" and nomEntra != "" and prenoEntra != "" and DtNaiss != "" and nation != ""):
            try:
                entr=Personne()
                entr.CIN=cin
                entr.Nom=nomEntra
                entr.Prenom=prenoEntra
                dat=DtNaiss
                dt=(datetime.strptime(dat,"%d/%m/%Y")).date()
                entr.DateNaissance=dt
                entr.Nationalite=nation

                DT = (datetime.strptime(DtCrea, "%d/%m/%Y")).date()
                equipe=Equipe(nomEq,DT,ville,entr)
                existe=False
                for eq in Equipe.T_Equipe:
                    if equipe.Nom == eq.Nom:
                        existe=True
                if existe==False:
                    Equipe.T_Equipe.append(equipe)
                    messagebox.showinfo("AJouter Equipe","Equipe est Ajouté avec Success")
                else:
                    messagebox.showerror("AJouter Equipe", "Equipe n'est pas Ajouté car déja existe")
            except ValueError:
                messagebox.showerror("Mauvaise Saisir","La date a forme (jj/mm/aaaa)!!!!")

        else:
            messagebox.showerror("Mauvaise Saisir","Donner Tous Les Information D'Equipe !!!!!!")




