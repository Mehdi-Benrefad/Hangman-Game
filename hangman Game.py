import random
import sys, os

liste_des_mots = ["king", "computer", "laptop", "help", "engineering", "python", "Pendu"]

#fonction qui permet de choisir un mot de la liste
def choisir(liste_des_mots):
    mot = random.choice(liste_des_mots)
    return mot.upper()

#fonction qui demare le jeu sur le mot choisis
def jouer(mot):
    #variable qui permet d'afficher des tirets pour chaque lettre du mot
    mot_completion = "_" * len(mot)
    #variable pour definir l'etat du jeu
    guessed = False
    #pour ne pas penaliser l'utilisateur plusieurs fois a la meme erreur on a besoin de:
    #liste des lettres devinees
    lettres_devinees = []
    #liste des mots devinees
    mots_devines = []
    essais = 6
    print("****************************************")
    print("*           JEU DE PENDU               *")
    print("****************************************")
    #afficher l'etat de pendu
    print(afficher_pendu(essais))
    #afficher les tirets qui symbolisent le mot
    print(mot_completion)
    print("\n")

    #Tant que le nombre d'essais n'est pas consomé et le mot reste non devine on repete
    while not guessed and essais > 0:
        guess = input("Entrer un mot ou une lettre pour deviner le mot: ").upper()
        #print("\n"*1000)
        #Pour netoyer la console
        clear = lambda: os.system('cls')
        clear()
        if len(guess) == 1 and guess.isalpha():

            if guess in lettres_devinees:
                print("vous avez deja essaye ", guess, "!")
            elif guess not in mot:
                print(guess, "ne figure pas dans le mot :(")
                essais -= 1
                lettres_devinees.append(guess)
            else:
                print("Bravo,", guess, "existe!")
                lettres_devinees.append(guess)
                #On transforme le mot en liste
                mot_as_list = list(mot_completion)
                #recupere les emplacement de la lettre devinee du mot
                indices = [i for i, letter in enumerate(mot) if letter == guess]
                #pour chaque indice on remplace le tiret par la lettre devinee
                for index in indices:
                    mot_as_list[index] = guess
                #mot_completion = mot_as_list
                #On transforme la liste en une chaine de caracteres
                mot_completion = "".join(mot_as_list)
                #si le mot de completion ne contient pas de tirets, c'est gagne
                if "_" not in mot_completion:
                    guessed = True
        #Si l'utilisateur essaye de tester le mot tout  entier
        elif len(guess) == len(mot) and guess.isalpha():
            if guess in mots_devines:
                print("vous avez deja essaye ce mot ", guess, "!")
            elif guess != mot:
                print(guess, " est incorecte :(")
                essais -= 1
                mots_devines.append(guess)
            else:
                guessed = True
                mot_completion = mot
        else:
            print("invalid input")

        print(afficher_pendu(essais))
        print(mot_completion)
        print("\n")

    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of essais. The word was " + mot + ". Maybe next time!")




#fonction qui permet d'afficher le pendu
def afficher_pendu(essais):
    etapes = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                   """
    ]
    return etapes[essais]


#def main():
mot = choisir(liste_des_mots)
jouer(mot)
while input("Voulez vous rejouer? (Y/N) ").upper() == "Y":
    mot = choisir(liste_des_mots)
    jouer(mot)



#cela implique que le module est exécuté de manière autonome par l'utilisateur et que nous pouvons effectuer les actions appropriées correspondantes.
#if __name__ == "__main__":
#    main()


#C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe "hangman Game.py"
