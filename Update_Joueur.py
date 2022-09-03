from tkinter import *
from LES_Classe import *
from datetime import datetime
from tkinter.ttk import Combobox
from tkinter import messagebox

class Update_Joueur(Tk):
    def __init__(self):
        super().__init__()
        self.title("Modifier Joueur")
        self.geometry("400x300")
        self.Initialise()
        self.bind("<Map>", self.load())


    def load(self):
        self.ListNom = []
        for equi in Equipe.T_Equipe:
            self.ListNom.append(equi.Nom)
        self.CmpNomEqui["values"] = self.ListNom
        self.CmpPoste["values"]=["GK","CB","RB","LB","CM","CDM","CAM","RW","LW","ST"]

    def Initialise(self):
        self.VarCin = StringVar(self)
        self.VarNom = StringVar(self)
        self.VarPrenom = StringVar(self)
        self.VarDtNaiss = StringVar(self)
        self.VarNum = StringVar(self)
        self.VarNatio = StringVar(self)

        self.lbl1 = Label(self, text="CIN  :").place(x=20,y=50)
        self.lbl2 = Label(self, text="Nom  :").place(x=20, y=80)
        self.lbl3 = Label(self, text="Prénom  :").place(x=20, y=110)
        self.lbl4 = Label(self, text="Date Naissance  :").place(x=20, y=140)
        self.lbl5 = Label(self, text="Numéro  :").place(x=20, y=170)
        self.lbl6 = Label(self, text="Poste  :").place(x=20, y=200)
        self.lbl7 = Label(self, text="Nationalité  :").place(x=20, y=230)
        self.lbl8 = Label(self, text="Equipe  :").place(x=20, y=20)

        self.entCin=Entry(self,textvariable=self.VarCin)
        self.entCin.place(x=130,y=50)
        self.entNom = Entry(self, textvariable=self.VarNom)
        self.entNom.place(x=130, y=80)
        self.entPrenom = Entry(self, textvariable=self.VarPrenom)
        self.entPrenom.place(x=130, y=110)
        self.entDtNaiss = Entry(self, textvariable=self.VarDtNaiss)
        self.entDtNaiss.place(x=130, y=140)
        self.entNum = Entry(self, textvariable=self.VarNum)
        self.entNum.place(x=130, y=170)
        self.entNation = Entry(self, textvariable=self.VarNatio)
        self.entNation.place(x=130, y=230)

        self.CmpPoste = Combobox(self)
        self.CmpPoste.place(x=130, y=200)

        self.CmpNomEqui = Combobox(self)
        self.CmpNomEqui.place(x=130, y=20)

        self.bntSupprimer = Button(self, text="Modifier Joueur",command=self.Modifier_Joueur)
        self.bntSupprimer.place(x=130, y=260)

        self.btnVider = Button(self, text="Vider", command=self.Vider_Click, width=6)
        self.btnVider.place(x=250, y=260)

    def Vider_Click(self):
        self.VarCin.set("")
        self.VarNom.set("")
        self.VarPrenom.set("")
        self.VarDtNaiss.set("")
        self.VarNum.set("")
        self.VarNatio.set("")
        self.CmpPoste.set("")
        self.CmpNomEqui.set("")

    def Modifier_Joueur(self):
        cin = self.VarCin.get()
        nom = self.VarNom.get()
        prenom = self.VarPrenom.get()
        dtNaissance = self.VarDtNaiss.get()
        numero = self.VarNum.get()
        poste = self.CmpPoste.get()
        nationalite = self.VarNatio.get()
        nomequipe = self.CmpNomEqui.get()
        if (cin != "" and nom != "" and prenom != "" and dtNaissance != "" and numero != "" and poste in self.CmpPoste["values"] and nationalite != "" and nomequipe in self.ListNom):
            try:
                numero = int(self.VarNum.get())
                if numero <= 99 and numero >= 1:
                    J = Joueur()
                    J.CIN = cin
                    J.Nom = nom
                    J.Prenom = prenom
                    J.DateNaissance = (datetime.strptime(dtNaissance, "%d/%m/%Y")).date()
                    J.Nationalite = nationalite
                    J.Numero = numero
                    J.Poste = poste
                    equipe = Equipe.Find_Equipe(nomequipe)
                    test=equipe.Update_Joueur_Prin(J)
                    if test == True:
                        messagebox.showinfo("Modifié Joueur", "Joueur est Modifié avec succées")
                    else:
                        messagebox.showerror("Modifié Joueur", "Joueur n'est pas Modifié car déja existe")
                else:
                    messagebox.showerror("Mauvaise Saisir", "Donner le numéro entre 1 et 99")
            except ValueError:
                messagebox.showerror("Mauvaise Saisir", "Donner Le Numéro Entier Et La date a forme (jj/mm/aaaa)!!!!")
        else:
            messagebox.showerror("Mauvaise Saisir", "Donner Tous Les Informations de Joueur, il faut que Informations existe")