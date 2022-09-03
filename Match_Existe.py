from tkinter import *


class Match_Existe(Tk):
    def __init__(self,match):
        super().__init__()
        self.title(match.EquipeLocale.Nom+"     VS     "+match.EquipeVisiteur.Nom)
        self.geometry("1300x550")
        self.Match=match
        self.Initialise()
        self.bind("<Map>", self.Load())

    def Load(self):
        self.VarJournee.set(self.Match.Journee)
        self.VarDateMatch.set(self.Match.DateMatch)
        self.VarLieu.set(self.Match.Lieu)
        self.VarEqLocale.set(self.Match.EquipeLocale.Nom)
        self.VarEqVisiteur.set(self.Match.EquipeVisiteur.Nom)
        self.VarButLocale.set(str(len(self.Match.ListeButLocal)))
        self.VarButVisiteur.set(str(len(self.Match.ListeButVisiteur)))
        T_ButLocale=[]
        for but in self.Match.ListeButLocal:
            ch=str(but.Minute)+"  ---  "
            num=int(but.Numero)
            ListeJoueur=self.Match.EquipeLocale.ListJoueurPrin
            for j in ListeJoueur:
                if j.Numero == num :
                    ch+= str(j)
            T_ButLocale.append(ch)
        self.ListeButLocale.set(T_ButLocale)
        T_ButVisiteur = []
        for but in self.Match.ListeButVisiteur:
            ch = str(but.Minute) + "  ---  "
            num = int(but.Numero)
            ListeJoueur = self.Match.EquipeVisiteur.ListJoueurPrin
            for j in ListeJoueur:
                if j.Numero == num:
                    ch += str(j)
            T_ButVisiteur.append(ch)
        self.ListeButVisiteur.set(T_ButVisiteur)

        T_CarteJeLocale = []
        for carte in self.Match.ListeCarte_Jeune_Locale:
            ch = str(carte.Minute) + "  ---  "
            num = int(carte.Numero)
            ListeCarte = self.Match.EquipeLocale.ListJoueurPrin
            for j in ListeCarte:
                if j.Numero == num:
                    ch += str(j)
            T_CarteJeLocale.append(ch)
        self.ListeCarteJLocale.set(T_CarteJeLocale)

        T_CarteRouLocale = []
        for but in self.Match.ListeCarte_Rouge_Locale:
            ch = str(but.Minute) + "  ---  "
            num = int(but.Numero)
            ListeCarte = self.Match.EquipeLocale.ListJoueurPrin
            for j in ListeCarte:
                if j.Numero == num:
                    ch += str(j)
            T_CarteRouLocale.append(ch)
        self.ListeCarteRLocale.set(T_CarteRouLocale)


        T_CarteJeVisiteur = []
        for carte in self.Match.ListeCarte_Jeune_Visiteur:
            ch = str(carte.Minute) + "  ---  "
            num = int(carte.Numero)
            ListeCarte = self.Match.EquipeVisiteur.ListJoueurPrin
            for j in ListeCarte:
                if j.Numero == num:
                    ch += str(j)
            T_CarteJeVisiteur.append(ch)
        self.ListeCarteJVisiteur.set(T_CarteJeVisiteur)

        T_CarteRouVisiteur = []
        for but in self.Match.ListeCarte_Rouge_Visiteur:
            ch = str(but.Minute) + "  ---  "
            num = int(but.Numero)
            ListeCarte = self.Match.EquipeVisiteur.ListJoueurPrin
            for j in ListeCarte:
                if j.Numero == num:
                    ch += str(j)
            T_CarteRouVisiteur.append(ch)
        self.ListeCarteRVisiteur.set(T_CarteRouVisiteur)

        self.CINArbitreCentre.set(self.Match.ArbitreCentre.CIN)
        self.NomArbitreCentre.set(self.Match.ArbitreCentre.Nom)
        self.PrenomArbitreCentre.set(self.Match.ArbitreCentre.Prenom)
        self.DateNaissArbitreCentre.set(self.Match.ArbitreCentre.DateNaissance)
        self.NationaliteArbitreCentre.set(self.Match.ArbitreCentre.Nationalite)
        self.PositionArbitreCentre.set(self.Match.ArbitreCentre.Position)

        self.CINArbitreToucheD.set(self.Match.ArbitreToucheDroit.CIN)
        self.NomArbitreToucheD.set(self.Match.ArbitreToucheDroit.Nom)
        self.PrenomArbitreToucheD.set(self.Match.ArbitreToucheDroit.Prenom)
        self.DateNaissArbitreToucheD.set(self.Match.ArbitreToucheDroit.DateNaissance)
        self.NationaliteArbitreToucheD.set(self.Match.ArbitreToucheDroit.Nationalite)
        self.PositionArbitreToucheD.set(self.Match.ArbitreToucheDroit.Position)

        self.CINArbitreToucheG.set(self.Match.ArbitreToucheGouche.CIN)
        self.NomArbitreToucheG.set(self.Match.ArbitreToucheGouche.Nom)
        self.PrenomArbitreToucheG.set(self.Match.ArbitreToucheGouche.Prenom)
        self.DateNaissArbitreToucheG.set(self.Match.ArbitreToucheGouche.DateNaissance)
        self.NationaliteArbitreToucheG.set(self.Match.ArbitreToucheGouche.Nationalite)
        self.PositionArbitreToucheG.set(self.Match.ArbitreToucheGouche.Position)

    def Initialise(self):
        #----- Les Variables ----
        self.VarJournee = StringVar(self)
        self.VarDateMatch = StringVar(self)
        self.VarLieu = StringVar(self)
        self.VarEqLocale = StringVar(self)
        self.VarEqVisiteur = StringVar(self)
        self.VarButLocale = StringVar(self)
        self.VarButVisiteur = StringVar(self)
        self.ListeButLocale = StringVar(self)
        self.ListeButVisiteur = StringVar(self)
        self.ListeCarteJLocale = StringVar(self)
        self.ListeCarteRLocale = StringVar(self)
        self.ListeCarteJVisiteur = StringVar(self)
        self.ListeCarteRVisiteur = StringVar(self)

        self.CINArbitreCentre = StringVar(self)
        self.NomArbitreCentre = StringVar(self)
        self.PrenomArbitreCentre = StringVar(self)
        self.DateNaissArbitreCentre = StringVar(self)
        self.NationaliteArbitreCentre = StringVar(self)
        self.PositionArbitreCentre = StringVar(self)

        self.CINArbitreToucheD = StringVar(self)
        self.NomArbitreToucheD = StringVar(self)
        self.PrenomArbitreToucheD = StringVar(self)
        self.DateNaissArbitreToucheD = StringVar(self)
        self.NationaliteArbitreToucheD = StringVar(self)
        self.PositionArbitreToucheD = StringVar(self)

        self.CINArbitreToucheG = StringVar(self)
        self.NomArbitreToucheG = StringVar(self)
        self.PrenomArbitreToucheG = StringVar(self)
        self.DateNaissArbitreToucheG = StringVar(self)
        self.NationaliteArbitreToucheG = StringVar(self)
        self.PositionArbitreToucheG = StringVar(self)

        # --- Label et Entry
        self.lbl1 = Label(self,text="Journée :").place(x=20,y=20)
        self.lbl2 = Label(self, text="Date de Match :").place(x=240, y=20)
        self.lbl3 = Label(self, text="Lieu de Match :").place(x=500, y=20)

        self.entJournee=Entry(self,textvariable=self.VarJournee).place(x=80,y=20)
        self.entDateMatch=Entry(self,textvariable=self.VarDateMatch).place(x=330,y=20)
        self.entLieu=Entry(self,textvariable=self.VarLieu).place(x=600,y=20)

        self.lbl4 = Label(self, textvariable=self.VarEqLocale).place(x=200, y=70)
        self.lbl5 = Label(self, textvariable=self.VarButLocale).place(x=320, y=70)
        self.lbl6 = Label(self, text="       :     ").place(x=340, y=70)
        self.lbl7 = Label(self, textvariable=self.VarEqVisiteur).place(x=470, y=70)
        self.lbl8 = Label(self, textvariable=self.VarButVisiteur).place(x=400, y=70)

        self.lbl9 = Label(self, text="Les Buts  :").place(x=170, y=110)
        self.ListeButL=Listbox(self,listvariable=self.ListeButLocale,width=55,height=6).place(x=20,y=130)

        self.lbl10 = Label(self, text="Les Cartes Jeune  :").place(x=155, y=240)
        self.ListeCJL = Listbox(self, listvariable=self.ListeCarteJLocale, width=55, height=6).place(x=20, y=260)

        self.lbl11 = Label(self, text="Les Cartes Rouge  :").place(x=155, y=370)
        self.ListeCRL = Listbox(self, listvariable=self.ListeCarteRLocale, width=55, height=6).place(x=20, y=390)

        self.lbl12 = Label(self, text="Les Buts  :").place(x=510, y=110)
        self.ListeButV = Listbox(self, listvariable=self.ListeButVisiteur, width=55, height=6).place(x=370, y=130)

        self.lbl13 = Label(self, text="Les Cartes Jeune  :").place(x=500, y=240)
        self.ListeCJV = Listbox(self, listvariable=self.ListeCarteJVisiteur, width=55, height=6).place(x=370, y=260)

        self.lbl14 = Label(self, text="Les Cartes Rouge  :").place(x=500, y=370)
        self.ListeCRV = Listbox(self, listvariable=self.ListeCarteRVisiteur, width=55, height=6).place(x=370, y=390)



        self.lbl15 = Label(self, text="L'Arbitre Centre  :").place(x=750, y=20)
        self.lbl16 = Label(self, text="CIN  :").place(x=770, y=40)
        self.entCinArCentre=Entry(self,textvariable=self.CINArbitreCentre).place(x=830, y=40)
        self.lbl17 = Label(self, text="Nom  :").place(x=770, y=70)
        self.entNomArCentre = Entry(self, textvariable=self.NomArbitreCentre).place(x=830, y=70)
        self.lbl18 = Label(self, text="Prénom  :").place(x=770, y=100)
        self.entPrenomArCentre = Entry(self, textvariable=self.PrenomArbitreCentre).place(x=830, y=100)
        self.lbl19 = Label(self, text="Date de Naissace  :").place(x=980, y=40)
        self.entCinArCentre = Entry(self, textvariable=self.DateNaissArbitreCentre).place(x=1090, y=40)
        self.lbl20 = Label(self, text="Nationalité  :").place(x=980, y=70)
        self.entNomArCentre = Entry(self, textvariable=self.NationaliteArbitreCentre).place(x=1090, y=70)
        self.lbl21 = Label(self, text="Position  :").place(x=980, y=100)
        self.entPrenomArCentre = Entry(self, textvariable=self.PositionArbitreCentre).place(x=1090, y=100)

        self.lbl22 = Label(self, text="L'Arbitre Touche Droit  :").place(x=750, y=150)
        self.lbl23 = Label(self, text="CIN  :").place(x=770, y=170)
        self.entCinArTD= Entry(self, textvariable=self.CINArbitreToucheD).place(x=830, y=170)
        self.lbl24 = Label(self, text="Nom  :").place(x=770, y=200)
        self.entNomArTD = Entry(self, textvariable=self.NomArbitreToucheD).place(x=830, y=200)
        self.lbl25 = Label(self, text="Prénom  :").place(x=770, y=230)
        self.entPrenomArTD = Entry(self, textvariable=self.PrenomArbitreToucheD).place(x=830, y=230)
        self.lbl26 = Label(self, text="Date de Naissace  :").place(x=980, y=170)
        self.entCinArTD = Entry(self, textvariable=self.DateNaissArbitreToucheD).place(x=1090, y=170)
        self.lbl27 = Label(self, text="Nationalité  :").place(x=980, y=200)
        self.entNomArTD = Entry(self, textvariable=self.NationaliteArbitreToucheD).place(x=1090, y=200)
        self.lbl28 = Label(self, text="Position  :").place(x=980, y=230)
        self.entPrenomArTD = Entry(self, textvariable=self.PositionArbitreToucheD).place(x=1090, y=230)

        self.lbl29 = Label(self, text="L'Arbitre Touche Droit  :").place(x=750, y=280)
        self.lbl30 = Label(self, text="CIN  :").place(x=770, y=300)
        self.entCinArTG = Entry(self, textvariable=self.CINArbitreToucheG).place(x=830, y=300)
        self.lbl31 = Label(self, text="Nom  :").place(x=770, y=330)
        self.entNomArTG = Entry(self, textvariable=self.NomArbitreToucheG).place(x=830, y=330)
        self.lbl32 = Label(self, text="Prénom  :").place(x=770, y=360)
        self.entPrenomArTG = Entry(self, textvariable=self.PrenomArbitreToucheG).place(x=830, y=360)
        self.lbl33 = Label(self, text="Date de Naissace  :").place(x=980, y=300)
        self.entCinArTG = Entry(self, textvariable=self.DateNaissArbitreToucheG).place(x=1090, y=300)
        self.lbl34 = Label(self, text="Nationalité  :").place(x=980, y=330)
        self.entNomArTG = Entry(self, textvariable=self.NationaliteArbitreToucheG).place(x=1090, y=330)
        self.lbl35 = Label(self, text="Position  :").place(x=980, y=360)
        self.entPrenomArTG = Entry(self, textvariable=self.PositionArbitreToucheG).place(x=1090, y=360)

