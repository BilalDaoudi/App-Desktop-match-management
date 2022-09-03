from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
class Delete_Arbitre(Tk):
    def __init__(self):
        super().__init__()
        self.title("Supprimer Arbitre")
        self.geometry("300x150")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        Liste_Cin=[]
        for arbitre in Arbire.T_Arbitres:
            Liste_Cin.append(arbitre.CIN)
        self.CmpCin["values"]=Liste_Cin

    def Initialise(self):
        self.lbl1 = Label(self, text="CIN de Arbitre  :").place(x=20,y=20)

        self.CmpCin = Combobox(self)
        self.CmpCin.place(x=120, y=20)

        self.btnAjouter = Button(self, text="Supprimer Arbitre",command=self.Delete_Arbitre)
        self.btnAjouter.place(x=100, y=70)

    def Delete_Arbitre(self):
        cin=self.CmpCin.get()
        if cin in self.CmpCin["values"]:
            Ar=Arbire.Find_Arbire(cin)
            Test=messagebox.askyesno("Supprimer Arbitre","Tu as Surre à Supprimer")
            if Test:
                Arbire.T_Arbitres.remove(Ar)
                messagebox.showinfo("Modifier Equipe", "Equipe est Supprimé")
        else:
            messagebox.showerror("Mauvaise Saisir","Choisir CIN de Arbitre")

