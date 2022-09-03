from tkinter import *
from datetime import datetime
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
class Update_Arbitre(Tk):
    def __init__(self):
        super().__init__()
        self.title("Modifier Arbitre")
        self.geometry("300x250")
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        Liste_Cin=[]
        for arbitre in Arbire.T_Arbitres:
            Liste_Cin.append(arbitre.CIN)
        self.CmpCin["values"]=Liste_Cin
        self.CmpPosition["values"]=["Center","Touche Droit","Touche Gouche"]


    def Initialise(self):
        self.lbl1 = Label(self, text="CIN                     :").place(x=20,y=20)
        self.lbl2 = Label(self, text="Nom                   :").place(x=20, y=50)
        self.lbl3 = Label(self, text="Prénom              :").place(x=20, y=80)
        self.lbl4 = Label(self, text="Date Naissance :").place(x=20, y=110)
        self.lbl5 = Label(self, text="Nationalité         :").place(x=20, y=140)
        self.lbl6 = Label(self, text="Position              :").place(x=20, y=170)

        self.VarNom = StringVar(self)
        self.VarPrenom = StringVar(self)
        self.VarDt = StringVar(self)
        self.VarNatio = StringVar(self)

        self.CmpCin = Combobox(self)
        self.CmpCin.place(x=120, y=20)

        self.entNom=Entry(self,textvariable=self.VarNom).place(x=120,y=50)
        self.entPrenom=Entry(self,textvariable=self.VarPrenom).place(x=120,y=80)
        self.entDate=Entry(self,textvariable=self.VarDt).place(x=120,y=110)
        self.entNatio=Entry(self,textvariable=self.VarNatio).place(x=120,y=140)
        self.CmpPosition=Combobox(self)
        self.CmpPosition.place(x=120,y=170)


        self.btnAjouter=Button(self,text="Modifier Arbitre",command=self.Ajouter_Arbitre)
        self.btnAjouter.place(x=100,y=210)

        self.btnVider = Button(self, text="Vider", command=self.Vider_Click, width=6)
        self.btnVider.place(x=220, y=210)

    def Vider_Click(self):
        self.VarNom.set("")
        self.VarPrenom.set("")
        self.VarDt.set("")
        self.VarNatio.set("")
        self.CmpPosition.set("")
        self.CmpCin.set("")


    def Ajouter_Arbitre(self):
        cin = self.CmpCin.get()
        nom = self.VarNom.get()
        prenom = self.VarPrenom.get()
        dt = self.VarDt.get()
        nationalite = self.VarNatio.get()
        position = self.CmpPosition.get()
        if cin in self.CmpCin["values"] :
            if nom != "" and prenom != "" and dt != "" and nationalite != "" and position in self.CmpPosition["values"] :
                try:
                    arbitre=Arbire.Find_Arbire(cin)
                    arbitre.Nom = nom
                    arbitre.Prenom = prenom
                    arbitre.DateNaissance = (datetime.strptime(dt, "%d/%m/%Y")).date()
                    arbitre.Nationalite = nationalite
                    arbitre.Position = position
                    messagebox.showinfo("Modifier Arbitre","Arbitre est Modifié")
                except:
                    messagebox.showerror("Mauvaise Saisir", "Donner La Date à sous Forme jj/mm/aaaa")
            else:
                messagebox.showerror("Mauvaise Saisir","Donner Tous Les Informations et Choisir Position !!!!!")
        else:
            messagebox.showerror("Mauvaise Saisir", "Choisir CIN !!!!!")


















