# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""


'''def creer_labyrinthe_depuis_chaine(chaine):
    print(chaine)'''

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""


    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = chaine
        '''self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)'''

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

