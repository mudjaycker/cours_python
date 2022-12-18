#les types simples
igiharuro = 3 #int
nyagakwabu = 4.897664637877256 #float
ijambo = "n'akana k'imyaka 3" #str

#les types complexes et contenneurs
urutonde = [1,3,4, "fennec"] #list
umurongo = (4, 7, 9, "fennec") #tuple !type immuable
aga_set = {-12,8, 4, 1, 0, 8, 1} #set !irakingira repetition des valeurs

kazinduzi = {"nom" : "fennec", "age" : 28}#dict

# Operations
addition = igiharuro + nyagakwabu #addition
soustraction = igiharuro - nyagakwabu #soustraction
division = igiharuro / nyagakwabu #division
multiplication = igiharuro * nyagakwabu #multiplication
modulo = igiharuro % nyagakwabu #modulo
exposant = igiharuro ** nyagakwabu #exposant


#Manipulation des types complexes et contenneurs
#Obtenir un contenu à partir du contenneur
position_urutonde = urutonde[3]
position_umurongo = umurongo[2]
position_aga_set = list(aga_set)[3] # !pour les set il faut d'abord les transformer en liste

position_kazinduzi = kazinduzi["age"] # ! pour	les dictionnaire on utilise la clé au lieu de la position