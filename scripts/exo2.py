# recuperer les 3 notes

grade1 = input("Enter first grade: ")
grade2 = input("Enter second grade: ")
grade3 = input("Enter third grade: ")

# type de variable
print(type(grade1))

##modification de mes notes en entier
#calculer la somme des 3 notes
somme = int(grade1) + int(grade2) + int(grade3)

##ou encore
somme = float(grade1) + float(grade2) + float(grade3)
print(f"la somme est : {somme:.2f}")

## calcul de cette moyenne (diviser par 3)
moyenne = somme / 3

## voir la somme des notes (afficher la moyenne)
print(moyenne)

#ou encore pour mettre 2 chiffres après la virgule pour les notes à virgule
print(f"la moyenne est : {moyenne:.2f}")

# comment tester la condition IF et ELSE (condition 1, condition 2)

## si la moyenne est supérieure ou égale à 16 ecrire "very good"
if moyenne >= 16:
    print("very good")

## si la moyenne est supérieure ou égale à 14 ecrire "good"
elif  moyenne >= 14:
    print("good")

## si la moyenne est supérieure ou égale à 12 ecrire "fairly good"
elif moyenne >= 12:
    print("fairly good")

## si la moyenne est supérieure ou égale à 10 ecrire "passable"
elif moyenne >= 10 :
    print("passable")

## si la moyenne est inférieure à 10 ecrire "failed"
elif moyenne < 10 :
    print("failed")

## pour toutes notes non prises en compte dans les autres conditions
else:
    print("message")








