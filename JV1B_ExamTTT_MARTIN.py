#1. Écrire la fonction permettant d’afficher la grille de jeu.

#plateau = [" "]*9

#def cadre():
#    for i in range(0, 9, 3):
#        print(" |  | ",(plateau[i]))
#        if i < 6:
#            print("-" * 9)
#while True:
#    cadre()
#    arret = int(input("stop"))

#2. Écrire la fonction permettant de jouer un O ou un X.

#while True:
#    cadre()
#    jeu = int(input("C'est au tour du joueur {joueur}. Entrez un nombre de 1 à 9 : "))
#   if plateau[jeu] == " ":
#        plateau[jeu] = joueur
#        joueur = "O" if joueur == "X" else "X"

#3. Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
#symboles sur une ligne verticale, horizontale, diagonale.

#def gagnant(symbole):
#    symbole = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
#joueur = "X"
#while True:
#    cadre()
#    jeu = int(input("Ecrit un nombre de 1 à 9 : "))-1
#    if plateau[jeu] == " ":
#        plateau[jeu] = joueur
#        if gagnant(joueur):
#            afficher_plateau()
#            print("Le joueur {joueur} a gagné !")
#        joueur = "O" if joueur == "X" else "X"


#4. Écrire la fonction vérifiant si la grille est complète.

#if " " not in plateau:
#    cadre()
#    print("Match nul !")

#5. Écrire un programme permettant de jouer à deux au Tic tac toe.

plateau = [" "]*9

def cadre():
    for i in range(0, 9, 3):
        print("  |   | ",(plateau[i]))
        if i < 6:
            print("-" * 9)
def gagnant(forme):
        forme = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
joueur = ("X")
while True:
    cadre()
    jeu = int(input(" un nombre de 1 à 9 : "))-1
    if plateau[jeu] == " ":
        plateau[jeu] = joueur
        if gagnant(joueur):
            cadre()
            print("Gagné !")
        joueur = "O" if joueur == "X" else "X"
    else:
        print("Case occupée. Réessayez.")
    if plateau[jeu] == " ":
        plateau[jeu] = joueur
        joueur = "O" if joueur == "X" else "X"

#6. Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de
#Puissance 4 ?

#Il suffira de donner de la gravité aux croix et aux ronds pour qu'ils tombent le plus bas quand ont les posent.