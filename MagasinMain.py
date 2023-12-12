#####import#####
import gestionMagasin as gestion
import caisseMagasin as caisse
import json
import os

#####fonction#####
def verification_float(txt : str, fois = 0)-> float:
    """
    Fonction vérifiant si la rentrer donner est bien du type float

    arguments :
        txt : le texte afficher pâr l'input
        fois: le nombre de fois que l'utilisateur c'est trompé
    
    """
    a = input(txt)
    try: float(a)*1
    except: return verification_float("re" + txt, fois + 1)
    else:
        if fois > 1: print("ENFIN !!")
        return float(a)

def verification_int(txt : str, fois = 0)-> int:
    """
    Fonction vérifiant si la rentrer donner est bien du type int

    arguments :
        txt : le texte afficher pâr l'input
        fois: le nombre de fois que l'utilisateur c'est trompé
    
    """
    a = input(txt)
    try: int(a)*1
    except: return verification_int("re" + txt, fois + 1)
    else:
        if fois > 1: print("ENFIN !!")
        return int(a)



    
    

#####programme#####
with open("mag.json" , "r") as f:
    jeu_video = json.load(f)

"""
jeu_video = {
        "KSP" : [10, 39.99], 
        "KSP2" : [10, 49.99], 
        "pacman" : [5, 150.36], 
        "adventur" : [9, 294.63], 
        "spacee invader" : [4, 359.33]
        }
"""


loop = True
os.system("cls")
print("Hello !")
while loop:
    
    loop_commande = True
    print("\nPour avoir un renseignement sur les actions possibles, tapez 'Help'\nVeuillez saisir une action")
    choix = input("-> ").lower()

    if choix == "fin": 
        os.system("cls")
        loop = False

    elif choix == "help": 
        os.system("cls")
        print("Les commandes sont : \n\tFin : Pour mettre fin au programme\n\tAjout : Pour ajouter un nouvel jeu video au magasin\n\tSupp : Pour supprimer un jeu video du magasin\n\tChanger_Prix : Pour changer le prix d'un jeu vidéo présenté en magasin\n\tChanger_Quantité : Pour changer la quantité d'un jeu video présenté en magasin\n\tCalcul_Stock : Pour calculer le prix total du stock en magasin\n\tAfficher : Pour afficher tous les jeux vidéos en vente\n\tAfficher_Objet : Pour afficher le prix et la quantité restante d'un jeu vidéo déjà existant\n\tCommande_Client : Pour calculer le montant de la commande d'un client\n")

    elif choix == "ajout":
        prix = False
        os.system("cls")
        nom = input("Saisir le nom du nouveau jeu vidéo : ").lower()
        while not(prix):
            prix = verification_float("Saisir le prix du nouveau jeu vidéo : ")
        gestion.Ajouter(jeu_video, nom, prix)

    elif choix == "supp":
        os.system("cls")
        nom = input("Saisir le nom du jeu vidéo à supprimer: ").lower()
        gestion.Supprimer(jeu_video, nom)
         
    elif choix == "changer_prix":
        prix = False
        os.system("cls")
        nom = input("Saisir le nom du jeu vidéo : ").lower()
        while not(prix): prix = verification_float("Saisir le nouveau prix du jeu vidéo : ")
        gestion.ChangerPrix(jeu_video, nom, prix)

    elif choix == "changer_quantité":
        quantite = False
        os.system("cls")
        nom = input("Saisir le nom du jeu vidéo : ").lower()
        while not(quantite): quantite = verification_int("Saisir la nouvelle quantite du jeu vidéo : ")
        gestion.ChangerQt(jeu_video, nom, quantite)

    elif choix == "calcul_stock":
        os.system("cls")
        print(f"La valeur du stock total est de : {gestion.ValeurStock(jeu_video)} €")

    elif choix == "afficher":
        os.system("cls")
        print("Les jeux vidéos ayant une entrée dans le magasin sont : ")
        caisse.Afficher(jeu_video)

    elif choix == "afficher_objet":
        os.system("cls")
        nom = input("Saisir le nom du jeu vidéo : ").lower()
        caisse.AffichObjet(jeu_video, nom)

    elif choix == "commande_client":
        os.system("cls")
        liste = []; tt = 0
        while loop_commande:
            jeu = input("Saisir le nom du jeu vidéo demandé par le client (ne rien saisir puis pour achever la commande et appuyez sur 'Entrée') : ")
            if jeu == "": loop_commande = False

            elif jeu in jeu_video.keys():
                quantite = False
                while not(quantite): quantite = verification_int("Saisir la quantité voulue du jeu vidéo : ")
                
                if quantite <= jeu_video[jeu][0]:
                    sous_commande = caisse.CommandeClient(jeu_video, jeu, quantite)
                    prix = quantite*jeu_video[jeu][1]
                    liste.append([jeu, quantite, prix])
                    tt += prix
                else: print(f"La quantié acutelle du jeu en stock est de {jeu_video[jeu][0]}, vous en demandez trop")

            else: print("Le jeu n'existe pas")

        os.system("cls")
        print("Vous avez commandé : ")
        for e in liste: print(f"\t -{e[1]} {e[0]} pour {e[2]} €") #afficher les centimes
        print(f"Pour un montant total de {tt} €") #afficher centimes

    else: 
        os.system("cls")
        print("ERREUR : cette commande n'existe pas")

with open("mag.json" , "w") as f: json.dump(jeu_video , f)
