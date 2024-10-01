## Pour tous elements appartenant à notre liste
## trouver la variable à itérer
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
for animal in animal_list:
    print(animal)

## ou
    print(f"mes elements de la list: {animal}")

############ correction
#!/usr/bin/env python3

# Créer la variable animal_list de type liste
# et assigner  la liste avec 4 valeurs
animal_list = ['cow', 'mouse', 'yeast', 'bacteria', "snake"]

## observer les indices et les elements de la liste
#print(list(enumerate(animal_list)))

# parcourir les elements de la liste en utilisant la boucle for
### en recuperant les indices et les elements avec enumerate
for indice, animal in enumerate(animal_list):
    print(f"indice : {indice}, element : {animal}")