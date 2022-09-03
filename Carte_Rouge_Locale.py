from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox

class Carte_Rouge_Locale(Tk):
    def __init__(self,match):
        super().__init__()
        self.match=match
        self.title("Carte Rouge de "+match.EquipeLocale.Nom)
        self.geometry("300x150")
        self.Inisialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        Liste_NumJ=[]
        for J in self.match.EquipeLocale.ListJoueurPrin:
            Liste_NumJ.append(J.Numero)
        self.CmpNumJ["values"]=Liste_NumJ


    def Inisialise(self):
        self.lbl1 = Label(self, text="Numéro Joueur :").place(x=20,y=20)
        self.lbl2 = Label(self, text="Minute  :").place(x=20, y=50)
        self.CmpNumJ=Combobox(self)
        self.CmpNumJ.place(x=120,y=20)

        self.VarMinute=StringVar(self)
        self.entMin=Entry(self,textvariable=self.VarMinute).place(x=120,y=50)

        self.btnGool=Button(self,text="Carte Rouge",command=self.Ajouter_Carte_Rouge_L)
        self.btnGool.place(x=100,y=90)

    def Ajouter_Carte_Rouge_L(self):
        num=self.CmpNumJ.get()
        try:
            minu=int(self.VarMinute.get())
            if num in self.CmpNumJ["values"]:
                if minu >= 1 and minu <= 120:
                    carte=Carte()
                    carte.Numero = num
                    carte.Minute = minu
                    self.match.ADD_Carte_Rouge_Local(carte)
                    messagebox.showinfo("Carte Rouge Locale", "Carte Rouge est Ajouté")
                else:
                    messagebox.showerror("Mauvaise Saisir", "Donner Minute Entre 1 et 120 !!! ")
            else:
                messagebox.showerror("Mauvaise Saisir", "Choisir Le Numéro de Joueur")
        except:
            messagebox.showerror("Mauvaise Saisir", "Minute est Entier")


















