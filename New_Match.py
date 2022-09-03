from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox
from LES_Classe import *
from tkinter import messagebox
from Match_Joue import Match_Joue

class New_Match(Tk):
    def __init__(self):
        super().__init__()
        self.title("New Match")
        self.geometry("370x320")
        self.Initialise()
        self.bind("<Map>", self.Load())


    def Load(self):
        self.T_ArbitreCentreCin=[]
        self.T_ArbitreTouchDroitCin = []
        self.T_ArbitreTouchGoucheCin = []
        for Arbitre in Arbire.T_Arbitres:
            if Arbitre.Position =="Center":
                self.T_ArbitreCentreCin.append(Arbitre.CIN)
            if Arbitre.Position =="Touche Droit":
                self.T_ArbitreTouchDroitCin.append(Arbitre.CIN)
            if Arbitre.Position =="Touche Gouche":
                self.T_ArbitreTouchGoucheCin.append(Arbitre.CIN)
        self.ComArbCentre["values"] = self.T_ArbitreCentreCin
        self.ComArbToucheDroit["values"] = self.T_ArbitreTouchDroitCin
        self.ComArbToucheGouche["values"] = self.T_ArbitreTouchGoucheCin

        self.T_Equipes=[]
        for equipe in Equipe.T_Equipe:
            if len(equipe.ListJoueurPrin) >= 11:
                self.T_Equipes.append(equipe.Nom)
        self.ComEqLocale["values"] = self.T_Equipes
        self.ComEqVisiteur["values"] = self.T_Equipes


    def Initialise(self):
        self.lbl1 = Label(self, text="Journée                       :").place(x=20,y=20)
        self.lbl2 = Label(self, text="Date                            :").place(x=20, y=50)
        self.lbl3 = Label(self, text="Lieu                             :").place(x=20, y=80)
        self.lbl4 = Label(self, text="Equipe Locale            :").place(x=20, y=110)
        self.lbl5 = Label(self, text="Equipe Visiteur          :").place(x=20, y=140)
        self.lbl6 = Label(self, text="Arbitre Centre            :").place(x=20, y=170)
        self.lbl7 = Label(self, text="Arbitre Touche Droit :").place(x=20, y=200)
        self.lbl8 = Label(self, text="Arbitre Touche Gouche :").place(x=20, y=230)

        self.VarJournee = StringVar(self)
        self.VarDate = StringVar(self)
        self.VarLieu = StringVar(self)

        self.entJournee=Entry(self,textvariable=self.VarJournee).place(x=150,y=20)
        self.entDate = Entry(self, textvariable=self.VarDate).place(x=150, y=50)
        self.entLieu = Entry(self, textvariable=self.VarLieu).place(x=150, y=80)

        self.ComEqLocale=Combobox(self)
        self.ComEqLocale.place(x=150,y=110)
        self.ComEqVisiteur = Combobox(self)
        self.ComEqVisiteur.place(x=150, y=140)
        self.ComArbCentre = Combobox(self)
        self.ComArbCentre.place(x=150, y=170)
        self.ComArbToucheDroit = Combobox(self)
        self.ComArbToucheDroit.place(x=150, y=200)
        self.ComArbToucheGouche = Combobox(self)
        self.ComArbToucheGouche.place(x=150, y=230)

        self.btnMatch=Button(self,text="Commencer Match",command=self.Commencer_Match)
        self.btnMatch.place(x=120,y=270)

    def Commencer_Match(self):
        journ=self.VarJournee.get()
        dt=self.VarDate.get()
        lieu=self.VarLieu.get()
        nomEqL=self.ComEqLocale.get()
        nomEqV=self.ComEqVisiteur.get()
        cinArC=self.ComArbCentre.get()
        cinArTD=self.ComArbToucheDroit.get()
        cinArTG=self.ComArbToucheGouche.get()
        if journ!="" and dt!="" and lieu!="" and nomEqL!="" and nomEqV!="" and cinArC!="" and cinArTD!="" and cinArTG!="":
            if nomEqL in self.T_Equipes and nomEqV in self.T_Equipes and cinArC in self.T_ArbitreCentreCin and cinArTD in self.T_ArbitreTouchDroitCin and cinArTG in self.T_ArbitreTouchGoucheCin:
                try:
                    datematch = (datetime.strptime(dt,"%d/%m/%Y")).date()
                    journee = int(journ)
                    equipeLocale = Equipe.Find_Equipe(nomEqL)
                    equipeVisiteur = Equipe.Find_Equipe(nomEqV)
                    arbitreCentre = Arbire.Find_Arbire(cinArC)
                    arbitreToucheDroit = Arbire.Find_Arbire(cinArTD)
                    arbitreToucheGouche = Arbire.Find_Arbire(cinArTG)
                    match=Match(journee,datematch,lieu,equipeLocale,equipeVisiteur,arbitreCentre,arbitreToucheDroit,arbitreToucheGouche)
                    MatchJoue=Match_Joue(match)
                    MatchJoue.mainloop()
                except:
                    messagebox.showerror("Mauvaise Saisir", "Donner Journée est Entier Et La Date a sous Forme jj/mm/aaaa !!!!")
            else:
                messagebox.showerror("Mauvaise Saisir", "Choisir Les Equipes Et Les Arbitres")
        else:
            messagebox.showerror("Mauvaise Saisir","Donner Tous Les Informations de Match")
