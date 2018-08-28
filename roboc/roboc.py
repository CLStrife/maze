# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle
from carte import Carte

# On charge les cartes existantes
cartes = []
saves = []
j = 0
start_point = []


def replace(chaine, i, character):
    c = chaine[:i] + character + chaine[i + 1:]
    return c

def afficher(laCarte):
    for ligne in laCarte[:len(laCarte)]:
        print(ligne)

def getStart_Poing(laCarte2):
    for i in range(9):
        for j in range(10):
            if laCarte2[i][j] == 'X':
                start_point = [i, j]
    return start_point

for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            maps = Carte(nom_carte, contenu)
            cartes.append(maps)

def save_game(one_map):
    with open("save\save.txt", "wb") as output:
        pickle.dump(one_map, output, pickle.HIGHEST_PROTOCOL)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter
if len(os.listdir("save")) != 0:
    for save_name in os.listdir("save"):
        if save_name.endswith(".txt"):
            file_path = os.path.join("save", save_name)
            save_map = save_name[:-3].lower()
            with open(file_path, "r") as save_file:
                contenu = save_file.read()
                save_game = Carte(save_name, contenu)
                saves.append(save_game)
    print("Partie sauvegardée :")
    for i, carte in enumerate(saves):
        print("  {} - {}".format(i + 1, carte.nom))

# ... Complétez le programme ...

choice = int(input("Veuillez choisir un labyrinthe :"))
carte = cartes[choice - 1]
print(carte.labyrinthe)

mvt = str
laCarte = carte.labyrinthe
laCarte2 = laCarte.split("\n")



coordinates = getStart_Poing(laCarte2)
x = coordinates[0]
y = coordinates[1]
'''Obtenir les coordonnées'''

while mvt != 'q':
    mvt = input("> ")
    mvt.lower()
    mvt2 = list(mvt)

    if mvt2[0] == 's':
        if laCarte2[x + 1][y] == "O":
            print("Vous ne pouvez pas passer")
        elif laCarte2[x + 1][y] == "." or laCarte2[x + 1][y] == " ":
            laCarte2[x + 1] = replace(laCarte2[x + 1], y, "X")
            laCarte2[x] = replace(laCarte2[x], y, " ")
            x = x + 1
    if mvt[0] == "n":
        if laCarte2[x - 1][y] == "O":
            print("Vous ne pouvez pas passer")
        elif laCarte2[x - 1][y] == "." or laCarte2[x - 1][y] ==" ":
            laCarte2[x - 1] = replace(laCarte2[x - 1], y, "X")
            laCarte2[x] = replace(laCarte2[x], y, " ")
            x = x - 1
    if mvt[0] == "e":
        if laCarte2[x][y + 1] == "O":
            print("Vous ne pouvez pas passer")
        elif laCarte2[x][y + 1] == "." or laCarte2[x][y + 1] == " ":
            laCarte2[x] = replace(laCarte2[x], y + 1, "X")
            laCarte2[x] = replace(laCarte2[x], y, " ")
            y = y + 1
    if mvt[0] == "o":
        if laCarte2[x][y - 1] == "O":
            print("Vous ne pouvez pas passer")
        elif laCarte2[x][y - 1] == "." or laCarte2[x][y - 1] == " ":
            laCarte2[x] = replace(laCarte2[x], y - 1, "X")
            laCarte2[x] = replace(laCarte2[x], y, " ")
            y = y - 1
    with open("save\save.txt", "wb") as f:
        for lign in laCarte2:
            f.write(str(lign) +"\n")

    """save_game(laCarte2)"""
    afficher(laCarte2)
"""enregistrer partie en cours, après chaque coups"""