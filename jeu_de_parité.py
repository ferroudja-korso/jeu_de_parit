import random

def jouer():
    nombre = random.randint(1, 50)
    print("J'ai choisi un nombre entre 1 et 100. Devinez-le !")

    while True:
        devine = int(input("Entrez votre réponse : "))

        if devine % 2 == 0:
            print("Le nombre est pair.")
        else:
            print("Le nombre est impair.")

        if devine == nombre:
            print("Bravo, vous avez gagné !")
            break
        else:
            print("Essayez encore.")

jouer()