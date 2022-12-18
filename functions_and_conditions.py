""" Les mot clés pour les conditions sont:
        if
        elif
        else
"""

# if ... else
age = 8

if age < 18:
    print("mineur")
else:
    print("majeur")

# if ... elif ... else
taille = 1.80

if taille == 1.90:
    print("long")
elif taille >= 2.0:
    print("trop long")
elif taille == 3.0:
    print("impossible")
else:
    print("taille normal")



# les functions:
#1er exemple
def afficher_le_nom(nom): # déclaration
    print(f"je suis {nom}")

afficher_le_nom(nom="tom") # appel (excecution)

#2em exemple
def faire_moyenne_de_deux_nombres(x, y): # déclaration
    somme = x + y
    moy = somme / 2
    print(f"la moyenne est {moy}") 

faire_moyenne_de_deux_nombres(x=56, y=45) # appel (excecution)

# fonction sans paramètre
def dire_bonjour(): # déclaration
    print("Bonjour le monde")

dire_bonjour() # appel (excecution)