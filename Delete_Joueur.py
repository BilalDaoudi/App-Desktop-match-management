from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
class Delete_Joueur(Tk):
    def __init__(self):
        super().__init__()
        self.title("Supprimer Joueur")
        self.geometry("350x150")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.ListNomEq=[]
        for equi in Equipe.T_Equipe:
            self.ListNomEq.append(equi.Nom)
        self.CmpNomEqui["values"]=self.ListNomEq

    def Initialise(self):
        self.lbl1=Label(self,text="Nom Equipe   :").place(x=20,y=20)
        self.CmpNomEqui=Combobox(self)
        self.CmpNomEqui.place(x=140,y=20)
        self.lbl2 = Label(self, text="CIN Joueur   :").place(x=20, y=50)
        self.VarCIN=StringVar(self)
        self.entCin = Entry(self,textvariable=self.VarCIN)
        self.entCin.place(x=140, y=50)

        self.bntSupprimer=Button(self,text="Supprimer Equipe",command=self.Supprimer_Joueur)
        self.bntSupprimer.place(x=130,y=100)
    def  Supprimer_Joueur(self):
        if self.CmpNomEqui.get() in self.ListNomEq and self.VarCIN.get() != "":
            equipe=Equipe.Find_Equipe(self.CmpNomEqui.get())
            test=equipe.Delete_Joueur_Prin(self.VarCIN.get())
            if test:
                messagebox.showinfo("Supprimer Joueur","Joueur est Supprimé ")
            else:
                messagebox.showinfo("Supprimer Joueur","Joueur n'est pas Existe ")
        else:
            messagebox.showerror("Mauvaise Saisir","Donner Nom Equipe et CIN Joueur !!!!!!!!!!")





