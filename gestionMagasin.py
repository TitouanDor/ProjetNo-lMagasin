def Ajouter(dicoco :dict, nom : str, prix : float) -> dict:
    """
    Fonction ajoutant un item dans un dictionnaire

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu dont on cherche les informations
        prix    : le prix du jeu
    """
    dicoco[nom] = [0, prix]
    return dicoco

def Supprimer(dicoco : dict, nom : str):
    """
    Fonction supprimant un item dans un dictionnaire

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu que l'on veut supprimer
    """

    del dicoco[nom]
    return dicoco

def ChangerPrix(dicoco : dict, nom : str, new_prix : float) -> dict:
    """
    Fonction changant le prix d'un item dans un dictionnaire

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu que l'on veut supprimer
        new_prix: le nouveaux prix de l'objet
    """

    dicoco[nom][1] = new_prix
    return dicoco

def ChangerQt(dicoco : dict, nom : str, new_qt : float) -> dict:
    """
    Fonction changant la quantité d'un item dans un dictionnaire

    Arguments :
        dicoco  : le dictionnaire
        nom     : le nom du jeu que l'on veut supprimer
        new_qt  : la nouvelle quantité de l'objet
    """
    dicoco[nom][0] = new_qt
    return dicoco
    
def ValeurStock(dicoco : dict) -> float:
    """
    Fonction estimant la valeur actuelle du magasin

    Argument :
        dicoco  : le dictionnaire
    """
    val = 0
    for e in dicoco.values(): val += e[1]* e[0]
    return val
