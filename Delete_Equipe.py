from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
class Delete_Equipe(Tk):
    def __init__(self):
        super().__init__()
        self.title("Supprimer Equipe")
        self.geometry("350x150")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.list=[]
        for equi in Equipe.T_Equipe:
            self.list.append(equi.Nom)
        self.CmpNomEqui["values"]=self.list

    def Initialise(self):
        self.lbl=Label(self,text="Nom Equipe   :").place(x=20,y=20)
        self.CmpNomEqui=Combobox(self)
        self.CmpNomEqui.place(x=140,y=20)

        self.bntSupprimer=Button(self,text="Supprimer Equipe",command=self.Supprimer_Equipe)
        self.bntSupprimer.place(x=130,y=70)
    def  Supprimer_Equipe(self):
        if self.CmpNomEqui.get() in self.list:
            test=messagebox.askyesno("Supprimer Equipe","Tu as Surre à Supprimer")
            if test:
                nom = self.CmpNomEqui.get()
                for equi in Equipe.T_Equipe:
                    if equi.Nom == nom:
                        Equipe.T_Equipe.remove(equi)
                messagebox.showinfo("Modifier Equipe", "Equipe est Supprimé")
        else:
            messagebox.showerror("Mauvaise Saisir", "Choisir Nom Equipe")



