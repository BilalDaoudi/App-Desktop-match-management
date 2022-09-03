from tkinter import *
from LES_Classe import *
from tkinter import messagebox

from Add_Equipe import Add_Equipe
from Liste_Equipe import ListeEquipe
from Delete_Equipe import Delete_Equipe
from Find_Equipe import Find_Equipe
from Update_Equipe import Update_Equipe

from Add_Joueur import Add_Joueur
from Liste_Joueurs import Liste_Joueur
from Delete_Joueur import Delete_Joueur
from Find_Joueur import Find_Joueur
from Update_Joueur import Update_Joueur

from Add_Arbitre import Add_Arbitre
from Liste_Arbitres import Liste_Arbitres
from Update_Arbitres import Update_Arbitre
from Delete_Arbitre import Delete_Arbitre
from Find_Arbitre import Find_Arbitre

from New_Match import New_Match
from Liste_Match import ListeMatch
from Find_Match import Find_Match

class Botola(Tk):
    def __init__(self):
        super().__init__()
        self.title("BOTOLA")
        self.geometry("400x250")
        self.Initialise()
        self.bind("<Map>",self.Load())

    def Load(self):
        Fichier = open("LesArbitres.txt","r")
        lignes = Fichier.readlines()
        T_Arbitres = []
        for li in lignes:
            if li != "\n":
                T_Arbitres.append(li)
        for arbitre in T_Arbitres:
            T_Info = arbitre.split(";")
            arbitre = Arbire()
            arbitre.CIN = T_Info[0]
            arbitre.Nom = T_Info[1]
            arbitre.Prenom = T_Info[2]
            arbitre.DateNaissance = T_Info[3]
            arbitre.Position = T_Info[4]
            arbitre.Nationalite = T_Info[5]
            Arbire.T_Arbitres.append(arbitre)
        Fichier.close()


        F=open("NomEquipes.txt","r")
        ligne = F.read()
        T_NomEq = []
        if ligne != "":
            T_NomEq=ligne.split(";")
        F.close()
        if len(T_NomEq) != 0:
            T_NomEq.remove(T_NomEq[len(T_NomEq) - 1])
            for nom in T_NomEq:
                Fich = open(nom+".txt","r")
                Lignes = Fich.readlines()
                T_Lignes=[]
                for L in Lignes:
                    if L != "\n":
                        T_Lignes.append(L)


                DtCreation = T_Lignes[1]
                ville = T_Lignes[2]
                AtributsEntra = T_Lignes[3].split(";")
                Entaineur = Personne()
                Entaineur.CIN = AtributsEntra[0]
                Entaineur.Nom = AtributsEntra[1]
                Entaineur.Prenom = AtributsEntra[2]
                Entaineur.DateNaissance = AtributsEntra[3]
                Entaineur.Nationalite = AtributsEntra[4]
                equipe=Equipe(nom,DtCreation,ville,Entaineur)

                for i in range(4,len(T_Lignes)):
                    Info_J = T_Lignes[i].split(";")
                    J = Joueur()
                    J.CIN = Info_J[0]
                    J.Nom = Info_J[1]
                    J.Prenom = Info_J[2]
                    J.DateNaissance = Info_J[3]
                    J.Nationalite = Info_J[4]
                    J.Poste = Info_J[5]
                    J.Numero = int(Info_J[6])
                    equipe.Add_Joueur_Prin(J)
                Equipe.T_Equipe.append(equipe)
                Fich.close()

        FI = open("LesMatch.txt", "r")
        LI = FI.readlines()
        T_NomMatch =[]
        if len(LI) != 0:
            T_NomMatch = LI[0].split(";")
        FI.close()
        if len(T_NomMatch) != 0:
            for nommatch in T_NomMatch:
                if nommatch != "":
                    nomM = nommatch + ".txt"
                    FICH = open(nomM, "r")
                    TLigne = FICH.readlines()
                    T_Inf = []
                    for Li in TLigne:
                        if Li != "\n":
                            T_Inf.append(Li)
                    T_InfoMatch = T_Inf[0].split(";")
                    journee = int(T_InfoMatch[0])
                    DateMatch = T_InfoMatch[1]
                    Lieu = T_InfoMatch[2]
                    equipeLoc = Equipe.Find_Equipe(T_InfoMatch[3])
                    equipeVis = Equipe.Find_Equipe(T_InfoMatch[4])
                    T_InfoArCenter = T_Inf[2].split(";")
                    arbitreCe = Arbire()
                    arbitreCe.CIN = T_InfoArCenter[0]
                    arbitreCe.Nom = T_InfoArCenter[1]
                    arbitreCe.Prenom = T_InfoArCenter[2]
                    arbitreCe.DateNaissance = T_InfoArCenter[3]
                    arbitreCe.Position = T_InfoArCenter[4]
                    arbitreCe.Nationalite =T_InfoArCenter[5]

                    T_InfoArTD = T_Inf[3].split(";")
                    arbitreTD = Arbire()
                    arbitreTD.CIN = T_InfoArTD[0]
                    arbitreTD.Nom = T_InfoArTD[1]
                    arbitreTD.Prenom = T_InfoArTD[2]
                    arbitreTD.DateNaissance = T_InfoArTD[3]
                    arbitreTD.Position = T_InfoArTD[4]
                    arbitreTD.Nationalite = T_InfoArTD[5]

                    T_InfoArTG = T_Inf[4].split(";")
                    arbitreTG = Arbire()
                    arbitreTG.CIN = T_InfoArTG[0]
                    arbitreTG.Nom = T_InfoArTG[1]
                    arbitreTG.Prenom = T_InfoArTG[2]
                    arbitreTG.DateNaissance = T_InfoArTG[3]
                    arbitreTG.Position = T_InfoArTG[4]
                    arbitreTG.Nationalite = T_InfoArTG[5]
                    match = Match(journee,DateMatch,Lieu,equipeLoc,equipeVis,arbitreCe,arbitreTD,arbitreTG)

                    T_InfoMatch = T_Inf[1].split("-")
                    T_InfoMatch.pop(len(T_InfoMatch)-1)
                    nbButL = int(T_InfoMatch[0])
                    for i in range(1,1+nbButL):
                        but = T_InfoMatch[i].split(";")
                        gool = Gool()
                        gool.Numero = but[0]
                        gool.Minute = but[1]
                        match.ADD_But_Local(gool)
                    nbButV = int(T_InfoMatch[nbButL+1])
                    for i in range(nbButL+2,nbButL+2+nbButV):
                        but = T_InfoMatch[i].split(";")
                        gool = Gool()
                        gool.Numero = but[0]
                        gool.Minute = but[1]
                        match.ADD_But_Visiteur(gool)


                    nbCarteJL = int(T_InfoMatch[nbButL+2+nbButV])
                    for i in range(nbButL+3+nbButV,nbButL+3+nbButV+nbCarteJL):
                        crt = T_InfoMatch[i].split(";")
                        carte = Carte()
                        carte.Numero = crt[0]
                        carte.Minute = crt[1]
                        match.ADD_Carte_Jeune_Local(carte)

                    nbCarteJV = int(T_InfoMatch[nbButL + 3 + nbButV + nbCarteJL])
                    for i in range(nbButL + 4 + nbButV + nbCarteJL,nbButL + 4 + nbButV + nbCarteJL + nbCarteJV):
                        crt = T_InfoMatch[i].split(";")
                        carte = Carte()
                        carte.Numero = crt[0]
                        carte.Minute = crt[1]
                        match.ADD_Carte_Jeune_Visiteur(carte)

                    nbCarteRL = int(T_InfoMatch[nbButL + 4 + nbButV + nbCarteJL + nbCarteJV])
                    for i in range(nbButL + 5 + nbButV + nbCarteJL + nbCarteJV,nbButL + 5 + nbButV + nbCarteJL + nbCarteJV+nbCarteRL):
                        crt = T_InfoMatch[i].split(";")
                        carte = Carte()
                        carte.Numero = crt[0]
                        carte.Minute = crt[1]
                        match.ADD_Carte_Rouge_Local(carte)
                    nbCarteRV = int(T_InfoMatch[nbButL + 5 + nbButV + nbCarteJL + nbCarteJV+nbCarteRL])
                    for i in range(nbButL + 6 + nbButV + nbCarteJL + nbCarteJV+nbCarteRL,nbButL + 6 + nbButV + nbCarteJL + nbCarteJV+nbCarteRL+nbCarteRV):
                        crt = T_InfoMatch[i].split(";")
                        carte = Carte()
                        carte.Numero = crt[0]
                        carte.Minute = crt[1]
                        match.ADD_Carte_Rouge_Visiteur(carte)
                    Match.Liste_Matchs.append(match)
                    FICH.close()
    def Initialise(self):
        self.MenuPrin = Menu(self)
        self.config(menu=self.MenuPrin)

        self.Equipe = Menu(self.MenuPrin)
        self.Equipe.add_command(label="ADD EQUIPE", command=self.Add_Equipe)
        self.Equipe.add_command(label="FIND EQUIPE", command=self.Recherche_Equipe)
        self.Equipe.add_command(label="DELETE EQUIPE", command=self.Delete_Equipe)
        self.Equipe.add_command(label="UPDATE EQUIPE", command=self.Modifier_Equipe)
        self.Equipe.add_separator()
        self.Equipe.add_command(label="LISTE EQUIPE", command=self.Liste_Equipe)
        self.MenuPrin.add_cascade(menu=self.Equipe, label="EQUIPE")

        self.Joueur = Menu(self.MenuPrin)
        self.Joueur.add_command(label="ADD JOUEUR", command=self.Add_Joueur)
        self.Joueur.add_command(label="FIND JOUEUR", command=self.Find_Joueur)
        self.Joueur.add_command(label="DELETE JOUEUR", command=self.Delete_Joueur)
        self.Joueur.add_command(label="UPDATE JOUEUR", command=self.Update_Joueur)
        self.Joueur.add_separator()
        self.Joueur.add_command(label="LISTE JOUEUR", command=self.Liste_Joueur)

        self.MenuPrin.add_cascade(menu=self.Joueur, label="JOUEUR")

        self.Arbitre = Menu(self.MenuPrin)
        self.Arbitre.add_command(label="ADD ARBITRE", command=self.Add_Arbitre)
        self.Arbitre.add_command(label="FIND ARBITRE", command=self.Find_Arbitre)
        self.Arbitre.add_command(label="DELETE ARBITRE", command=self.Delete_Arbitre)
        self.Arbitre.add_command(label="UPDATE ARBITRE", command=self.Update_Arbitre)
        self.Arbitre.add_separator()
        self.Arbitre.add_command(label="LISTE ARBITRE", command=self.Liste_Arbitre)

        self.MenuPrin.add_cascade(menu=self.Arbitre, label="ARBITRE")

        self.btnSauvEqui = Button(self, text="Sauvgarder Equipes", bg='gray', width=20, command=self.Suvgarder_Equipes)
        self.btnSauvEqui.place(x=130, y=20)

        self.btnSauvArbi = Button(self, text="Sauvgarder Arbitres", bg='gray', width=20, command=self.Suvgarder_Arbites)
        self.btnSauvArbi.place(x=130, y=50)

        self.btnList = Button(self, text="Liste Match", bg='gray', width=20, command=self.Liste_Match)
        self.btnList.place(x=130, y=140)

        self.btnList = Button(self, text="New Match", bg='gray', width=20, command=self.New_Match)
        self.btnList.place(x=130, y=110)

        self.btnSauvmatch = Button(self, text="Sauvgarder Match", bg='gray', width=20,command=self.Sauvgarder_Match)
        self.btnSauvmatch.place(x=130,y=80)

        self.btnFindMatch = Button(self, text="Rechercher Match", bg='gray', width=20, command=self.Rechercher_Match)
        self.btnFindMatch.place(x=130, y=170)


    def Suvgarder_Equipes(self):
        fich = open("NomEquipes.txt", "w")
        NomEquipe = ""
        for equipe in Equipe.T_Equipe:
            equipe.Sauvgarder()
            NomEquipe += equipe.Nom+";"
        fich.write(NomEquipe)
        fich.close()
        messagebox.showinfo("Sauvgarder Equipes", "Les Equipes est Sauvgardé ☻☻")
    def Suvgarder_Arbites(self):
        Arbire.Sauvgarder()
        messagebox.showinfo("Sauvgarder Arbitres", "Les Arbitres est Sauvgardé ☻☻")


    def Add_Equipe(self):
        Equi = Add_Equipe()
        Equi.mainloop()
    def Delete_Equipe(self):
        Equi = Delete_Equipe()
        Equi.mainloop()
    def Liste_Equipe(self):
        Liste = ListeEquipe()
        Liste.mainloop()
    def Recherche_Equipe(self):
        equi = Find_Equipe()
        equi.mainloop()
    def Modifier_Equipe(self):
        equi = Update_Equipe()
        equi.mainloop()

    def Add_Joueur(self):
        J = Add_Joueur()
        J.mainloop()
    def Liste_Joueur(self):
        ListeJ = Liste_Joueur()
        ListeJ.mainloop()
    def Delete_Joueur(self):
        J = Delete_Joueur()
        J.mainloop()
    def Find_Joueur(self):
        J = Find_Joueur()
        J.mainloop()
    def Update_Joueur(self):
        J = Update_Joueur()
        J.mainloop()

    def Add_Arbitre(self):
        Arbitre = Add_Arbitre()
        Arbitre.mainloop()
    def Liste_Arbitre(self):
        Arbitre = Liste_Arbitres()
        Arbitre.mainloop()
    def Update_Arbitre(self):
        Arbitre = Update_Arbitre()
        Arbitre.mainloop()
    def Delete_Arbitre(self):
        Arbitre = Delete_Arbitre()
        Arbitre.mainloop()
    def Find_Arbitre(self):
        Arbitre = Find_Arbitre()
        Arbitre.mainloop()

    def New_Match(self):
        match = New_Match()
        match.mainloop()

    def Sauvgarder_Match(self):
        F = open("LesMatch.txt", "w")
        LesMAtch = ""
        for match in Match.Liste_Matchs:
            LesMAtch += match.EquipeLocale.Nom+str(match.Journee)+match.EquipeVisiteur.Nom
            LesMAtch += ";"
        F.write(LesMAtch)
        F.close()

        for match in Match.Liste_Matchs:
            match.Sauvgarder()

        messagebox.showinfo("Sauvgarder Match","Les Match est Sauvgardé ☻☻")

    def Liste_Match(self):
        Liste = ListeMatch()
        Liste.mainloop()

    def Rechercher_Match(self):
        Match = Find_Match()
        Match.mainloop()


