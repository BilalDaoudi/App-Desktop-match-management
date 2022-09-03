from tkinter import *
from LES_Classe import *
from tkinter import messagebox
from But_Locale import But_Locale
from But_Visiteur import But_Visiteur
from Carte_Jeune_Locale import Carte_Jeune_Locale
from Carte_Jeune_Visiteur import Carte_Jeune_Visiteur
from Carte_Rouge_Locale import Carte_Rouge_Locale
from Carte_Rouge_Visiteur import Carte_Rouge_Visiteur


class Match_Joue(Tk):
    def __init__(self,match):
        super().__init__()
        self.title("Match "+match.EquipeLocale.Nom+" VS "+match.EquipeVisiteur.Nom)
        self.geometry("370x150")
        self.match=match
        self.Inisialise()

    def Inisialise(self):
        self.MenuPrin = Menu(self)
        self.config(menu=self.MenuPrin)

        self.But = Menu(self.MenuPrin)
        self.But.add_command(label="But Equipe Locale",command=self.Ajouter_But_Locale)
        self.But.add_command(label="But Equipe Visiteur",command=self.Ajouter_But_Visiteur)

        self.MenuPrin.add_cascade(menu=self.But, label="But")

        self.Carte = Menu(self.MenuPrin)
        self.Carte.add_command(label="Carte Jeune Eq. Locale",command=self.Ajouter_Carte_Jeune_Locale)
        self.Carte.add_command(label="Carte Jeune Eq. Visiteur",command=self.Ajouter_Carte_Jeune_Visiteur)
        self.Carte.add_command(label="Carte Rouge Eq. Locale",command=self.Ajouter_Carte_Rouge_Locale)
        self.Carte.add_command(label="Carte Rouge Eq. Visiteur",command=self.Ajouter_Carte_Rouge_Visiteur)

        self.MenuPrin.add_cascade(menu=self.Carte, label="Carte")

        self.VarNomLocale = StringVar(self)
        self.VarNomLocale.set(self.match.EquipeLocale.Nom)
        self.VarNomVisiteur = StringVar(self)
        self.VarNomVisiteur.set(self.match.EquipeVisiteur.Nom)
        self.VarButLocale = IntVar(self)
        self.VarButVisiteur = IntVar(self)

        self.lblLocale=Label(self,textvariable=self.VarNomLocale).place(x=50,y=35)
        self.lblButLocale = Label(self, textvariable=self.VarButLocale).place(x=140, y=35)
        self.lblPoit = Label(self, text="    :  ").place(x=150, y=35)
        self.lblVisiteur = Label(self, textvariable=self.VarNomVisiteur).place(x=220, y=35)
        self.lblButVisiteur = Label(self, textvariable=self.VarButVisiteur).place(x=180, y=35)

        self.btnMiseJour=Button(self,text="Mise à jour",command=self.Mise_jour_Match)
        self.btnMiseJour.place(x=90,y=85)
        self.btnFinMatch = Button(self, text="Fin match",command=self.Fin_Match)
        self.btnFinMatch.place(x=160, y=85)

    def Ajouter_But_Locale(self):
        but=But_Locale(self.match)
        but.mainloop()
    def Ajouter_But_Visiteur(self):
        but = But_Visiteur(self.match)
        but.mainloop()
    def Ajouter_Carte_Jeune_Locale(self):
        carte=Carte_Jeune_Locale(self.match)
        carte.mainloop()
    def Ajouter_Carte_Jeune_Visiteur(self):
        carte = Carte_Jeune_Visiteur(self.match)
        carte.mainloop()
    def Ajouter_Carte_Rouge_Locale(self):
        carte = Carte_Rouge_Locale(self.match)
        carte.mainloop()
    def Ajouter_Carte_Rouge_Visiteur(self):
        carte = Carte_Rouge_Visiteur(self.match)
        carte.mainloop()
    def Mise_jour_Match(self):
        self.VarButLocale.set(len(self.match.ListeButLocal))
        self.VarButVisiteur.set(len(self.match.ListeButVisiteur))
    def Fin_Match(self):
        journee=self.match.Journee
        nomEqLo=self.match.EquipeLocale.Nom
        nomEqVi = self.match.EquipeVisiteur.Nom
        match=Match.Find_Match(journee,nomEqLo,nomEqVi)
        if match == None:
            Match.Liste_Matchs.append(self.match)
            messagebox.showinfo("Ajouter Match","Match est Terminé")
        else:
            messagebox.showerror("Erreur","Match déja Terminé")
















