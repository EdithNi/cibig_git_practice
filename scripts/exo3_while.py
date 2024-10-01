#• Create a Python program exo3_while.py that displays all the elements of the animal_list using a while loop
# Given the following list: animal_list = ['cow', 'mouse', 'yeast', 'bacteria']

## objectif: afficher le contenu d'une liste avec while
##1 creer la liste en assignant valeur animal_list
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']

##2 parcourir la liste avec while y compris la condition d'arrèt

##3 comment obtenir cette condition

##4 condition d'arrèt et le nbr d'élement de la list

##4# stocker et extraire le nbr d'element list dans une variable ( lengh animal_list)
lengh_list_animal = len(animal_list)

### tant que index soit petit ou égal à taille (lengh_list_animal), ecrire la boucle while avec condition d'arrèt
i = 0
while i < lengh_list_animal:
    print(i, animal_list[i])
    i = i + 1

    # correction

    # Créer la variable animal_list de type liste
    # et assigner  la liste avec 4 valeurs
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
# print(animal_list[0])
# print(animal_list[1])
# print(animal_list[2])

# Parcourir la liste avec le while
# et afficher les élements de la liste un à un

# 1 - Extraire la taille de notre liste avec la fonction len(list)
# et on stocke la valeure retournée dans la variable legnth_animal_list
length_animal_list = len(animal_list)
print(f"La taille de mon tableau est de : {length_animal_list}\n")

# 2- Creer une variable indice qui va etre assignée à 0
indice = 0

# 3 - parcourir la liste avec while
# et la variable indice (compteur) + condition d arret
while indice < length_animal_list:
    # Afficher l element de la liste a l indice de la boucle
    print(f"----- Mon indice est : {indice}")
    print(f"Mon element lu est : {animal_list[indice]}\n")

    # a la fin de chaque boucle, on ajoute 1 à indice
    indice = indice + 1

print(f"A la fin de la boucle, mon indice est de : {indice} ")