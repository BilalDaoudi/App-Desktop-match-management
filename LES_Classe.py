class Personne:
    def __init__(self):
        self.CIN=""
        self.Nom=""
        self.Prenom = ""
        self.DateNaissance = None
        self.Nationalite = ""
    def __str__(self):
        return f"{self.CIN};{self.Nom};{self.Prenom};{self.DateNaissance};{self.Nationalite};"

class Joueur(Personne):
    def __init__(self):
        super().__init__()
        self.Poste=""
        self.Numero=0

    def __str__(self):
        ch=super().__str__()
        ch+=f"{self.Poste};{self.Numero}"
        return ch

class Arbire(Personne):
    T_Arbitres=[]
    @classmethod
    def Find_Arbire(cls, cin):
        for Arbitre in Arbire.T_Arbitres:
            if Arbitre.CIN == cin:
                return Arbitre
        return None

    @classmethod
    def Sauvgarder(cls):
        Fich=open("LesArbitres.txt","w")
        for Ar in Arbire.T_Arbitres:
            Fich.write(str(Ar)+"\n")
        Fich.close()

    def __init__(self):
        super().__init__()
        self.Position=""
    def __str__(self):
        ch=super().__str__()
        ch+=f"{self.Position}"
        return f"{self.CIN};{self.Nom};{self.Prenom};{self.DateNaissance};{self.Position};{self.Nationalite}"

class Equipe:
    T_Equipe=[]
    @classmethod
    def Find_Equipe(cls,nom):
        for equ in Equipe.T_Equipe:
            if equ.Nom == nom:
                return equ
        return None

    def __init__(self,nom,dt,ville,entrai):
        self.Nom=nom
        self.DateCreation=dt
        self.Ville=ville
        self.Entraineur=entrai
        self.ListJoueurPrin = []


    def __str__(self):
        return f"{self.Nom};{self.DateCreation};{self.Ville};{self.Entraineur}{len(self.ListJoueurPrin)}"

    def Find_Joueur_Prin(self,cin):
        for i in range(len(self.ListJoueurPrin)):
            if self.ListJoueurPrin[i].CIN == cin:
                return i
        return -1

    def Add_Joueur_Prin(self,J):
        test=self.Find_Joueur_Prin(J.CIN)
        if test == -1:
            self.ListJoueurPrin.append(J)
            return True
        else:
            return False
    def Delete_Joueur_Prin(self,cin):
        test=self.Find_Joueur_Prin(cin)
        if test != -1:
            self.ListJoueurPrin.pop(test)
            return True
        else:
            return False

    def Update_Joueur_Prin(self,J):
        test=self.Find_Joueur_Prin(J.CIN)
        if test != None:
            self.ListJoueurPrin[test] = J
            return True
        else:
            return False

    def Recherche_Num(self,Num):
        for i in range(len(self.ListJoueurPrin)):
            if self.ListJoueurPrin[i].Numero == Num:
                return i
        return -1

    def Sauvgarder(self):
        nom=self.Nom+".txt"
        Fich=open(nom,"w")
        Fich.write(self.Nom+"\n"+str(self.DateCreation)+"\n"+self.Ville)
        Fich.write("\n"+str(self.Entraineur)+"\n")
        for joeur in self.ListJoueurPrin:
            Fich.write(str(joeur)+"\n")
        Fich.close()


class Carte:
    def __init__(self):
        self.Numero=0
        self.Minute=0
    def __str__(self):
        return f"{self.Numero};{self.Minute}"

class Gool:
    def __init__(self):
        self.Numero=0
        self.Minute=0
    def __str__(self):
        return f"{self.Numero};{self.Minute}"


class Match:
    Liste_Matchs = []
    @classmethod
    def Find_Match(cls,j,NomEqL,NomEqV):
        for match in Match.Liste_Matchs:
            if match.Journee == j and match.EquipeLocale.Nom == NomEqL and match.EquipeVisiteur.Nom == NomEqV:
                return match
        return None


    def __init__(self,journee,DtMatch,Lieu,EqLocal,EqVisiteur,ArbCenter,ArbTouchDr,ArbTouchGo):
        self.Journee = journee
        self.DateMatch = DtMatch
        self.Lieu = Lieu
        self.EquipeLocale = EqLocal
        self.EquipeVisiteur = EqVisiteur
        self.ArbitreCentre = ArbCenter
        self.ArbitreToucheDroit = ArbTouchDr
        self.ArbitreToucheGouche = ArbTouchGo
        self.ListeButLocal = []
        self.ListeButVisiteur = []
        self.ListeCarte_Jeune_Locale = []
        self.ListeCarte_Jeune_Visiteur = []
        self.ListeCarte_Rouge_Locale = []
        self.ListeCarte_Rouge_Visiteur = []

    def ADD_But_Local(self,But):
        self.ListeButLocal.append(But)

    def ADD_But_Visiteur(self,But):
        self.ListeButVisiteur.append(But)

    def ADD_Carte_Jeune_Local(self,Carte):
        self.ListeCarte_Jeune_Locale.append(Carte)

    def ADD_Carte_Jeune_Visiteur(self,Carte):
        self.ListeCarte_Jeune_Visiteur.append(Carte)

    def ADD_Carte_Rouge_Local(self,Carte):
        self.ListeCarte_Rouge_Locale.append(Carte)

    def ADD_Carte_Rouge_Visiteur(self,Carte):
        self.ListeCarte_Rouge_Visiteur.append(Carte)

    def __str__(self):
        ch=f"{self.Journee}    \t{self.EquipeLocale.Nom}\t   {len(self.ListeButLocal)}     :    {len(self.ListeButVisiteur)}    \t{self.EquipeVisiteur.Nom} \n"
        return ch

    def Sauvgarder(self):
        nom=self.EquipeLocale.Nom+str(self.Journee)+self.EquipeVisiteur.Nom+".txt"
        Fich=open(nom,"w")
        ch=str(self.Journee)+";"+str(self.DateMatch)+";"+self.Lieu+";"+self.EquipeLocale.Nom+";"+self.EquipeVisiteur.Nom+";"
        Fich.write(ch)
        CH="\n"
        CH+=str(len(self.ListeButLocal))+"-"
        for but in self.ListeButLocal:
            CH+=str(but)+"-"

        CH+=str(len(self.ListeButVisiteur))+"-"
        for gool in self.ListeButVisiteur:
            CH+=str(gool)+"-"

        CH+=str(len(self.ListeCarte_Jeune_Locale))+"-"
        for carteJL in self.ListeCarte_Jeune_Locale:
            CH+=str(carteJL)+"-"

        CH+=str(len(self.ListeCarte_Jeune_Visiteur))+"-"
        for carteJV in self.ListeCarte_Jeune_Visiteur:
            CH+=str(carteJV)+"-"

        CH+=str(len(self.ListeCarte_Rouge_Locale))+"-"
        for carteRV in self.ListeCarte_Rouge_Locale:
            CH+=str(carteRV)+"-"

        CH+=str(len(self.ListeCarte_Rouge_Visiteur))+"-"
        for carteRV in self.ListeCarte_Rouge_Visiteur:
            CH +=str(carteRV)+"-"
        Fich.write(CH)
        Fich.write("\n" + str(self.ArbitreCentre))
        Fich.write("\n" + str(self.ArbitreToucheDroit))
        Fich.write("\n" + str(self.ArbitreToucheGouche))
        Fich.close()
















