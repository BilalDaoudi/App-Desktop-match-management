from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
from Match_Existe import Match_Existe
class Find_Match(Tk):
    def __init__(self):
        super().__init__()
        self.title("Rechercher Match")
        self.geometry("360x160")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.list = []
        for equi in Equipe.T_Equipe:
            self.list.append(equi.Nom)
        self.CMPNomEqL["values"] = self.list
        self.CMPNomEqV["values"] = self.list

    def Initialise(self):
        self.lbl1 = Label(self, text="Journee :").place(x=20, y=20)
        self.lbl2 = Label(self, text="Nom Equipe Locale :").place(x=20, y=50)
        self.lbl3 = Label(self, text="Nom Equipe Visiteur :").place(x=20, y=80)
        self.VarJournee= StringVar(self)
        self.entJournee = Entry(self,textvariable=self.VarJournee).place(x=140, y=20)

        self.CMPNomEqL = Combobox(self)
        self.CMPNomEqL.place(x=140, y=50)
        self.CMPNomEqV = Combobox(self)
        self.CMPNomEqV.place(x=140, y=80)

        self.btnRechercher = Button(self, text="Rechercher Match",command=self.Rechercher_Match)
        self.btnRechercher.place(x=110, y=120)

    def Rechercher_Match(self):
        if self.VarJournee.get() != "" and self.CMPNomEqV.get() != "" and self.CMPNomEqL.get() != "" :
            try:
                journee=int(self.VarJournee.get())
                eqLocale=self.CMPNomEqL.get()
                eqVisiteur=self.CMPNomEqV.get()
                m=Match.Find_Match(journee,eqLocale,eqVisiteur)
                if m != None:
                    Existe=Match_Existe(m)
                    Existe.mainloop()
                else:
                    messagebox.showinfo("Recherche Match", "Match n'est pas Existe !!!!!!!!!!!!!!")
            except:
                messagebox.showerror("Mauvaise Saisir", "Donner Journee Entier!!!!!!!!!!!!!!")
        else:
            messagebox.showerror("Mauvaise Saisir", "Donner le Journee Et Choisir Les Equipes !!!!!!!!!!!!!!")



