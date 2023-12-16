def Afficher(dicoco : dict) -> None:
    """
    Fonction affichant les clefs du dictionnaire

    Argument :
        dicoco : le dictionnaire
    """
    print("Les jeux vidéos ayant une entrée dans le magasin sont : ")
    for e in dicoco.keys(): print("\t -", e)

def AffichObjet(dicoco : dict, nom : str):
    """
    Fonction affichant la quantité et le prix d'un jeu donné

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu dont on cherche les informations
    """

    print("Quantité de l'objet : ", dicoco[nom][0])
    print("Le prix de l'objet : ", dicoco[nom][1])

def CommandeClient(dicoco : dict, produit : str, qte : int) -> float:
    """
    Fonction renvoyant le total d'une commande d'un seul produit mais en quatité variable

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu que l'on souhaite acheter
        qte     : la quantité de jeu acheté
    """

    if qte <= dicoco[produit][0]:
        dicoco[produit][0] -= qte
        return qte*dicoco[produit][1]
    
    else: return False