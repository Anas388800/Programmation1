
class Personnage :
    nom = "nom du joueur"
    prenom = "prenom du joueur"
    age = "age du joueur"
    puissance = "puissance du joueur"

    def __init__(self,nom,prenom,age,puissance,faiblesse) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.puissance = puissance
        self.__faiblesse = faiblesse    # on n'a pas accés à ça de l'exterieur " .__ "



Pers = Personnage("Goku","Son",38,"kameha","boo")
#Pers.nom = "Goku"

print(Pers)
print(Pers.nom)
print("")
print(Pers.faiblesse)




class Voiture :
    model = "model voiture"
    anneeCreation = "annee creation"
    alimentation = "type carburant"
    nbPlace = "nb place"
    puissance = "puissance"
    #coutFabri = "coutfabri"

    def __init__(self, model, anneeCreation,alimentation,nbPlace, puissance, coutFabri):
        self.model = model
        self.anneeCreation = anneeCreation
        self.alimentation = alimentation
        self.nbPlace = nbPlace
        self.puissance = puissance
        self.__coutFabri = coutFabri

auto = Voiture("BMW",2010,"Essence",8,110,1000)
print(auto)
print("avant effaçage : ",auto.model)
print(auto.nbPlace)


del auto.model
print("apres effaçage :",auto.model)

nu = int(input("premer chiffre"))
num = int(input("deuxeme chiffre"))

res = num * num
print("resultat = ",res)


print('My', 'Name', 'Is', 'James', sep='**')

print("une autre modif pour le texte")
print("une autre modif pour le texte22")