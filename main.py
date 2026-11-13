from marge import calculer_marge
from tva import calculer_tva
from interets import calculer_interets
from ventes import calculer_total_ventes


def afficher_menu():
    print("====================================")
    print(" BOITE A OUTILS DE GESTION COMMERCIALE")
    print("====================================")
    print("1. Calcul de la marge")
    print("2. Calcul de la TVA")
    print("3. Calcul des interets")
    print("4. Total des ventes")
    print("5. Quitter")


while True:
    afficher_menu()

    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Choix invalide")
        continue

    if choix == 1:
        achat = float(input("Prix d'achat HT : "))
        vente = float(input("Prix de vente HT : "))

        marge, taux_marge, taux_marque = calculer_marge(vente, achat)

        print("Marge :", marge)
        print("Taux de marge :", taux_marge, "%")
        print("Taux de marque :", taux_marque, "%")

    elif choix == 2:
        prix = float(input("Prix HT : "))
        taux = float(input("Taux TVA : "))

        tva, prix_ttc = calculer_tva(prix, taux)

        print("Montant TVA :", tva)
        print("Prix TTC :", prix_ttc)

    elif choix == 3:
        capital = float(input("Capital : "))
        taux = float(input("Taux d'interet : "))
        duree = float(input("Duree : "))

        resultat = calculer_interets(capital, taux, duree)
        print("Interets :", resultat)

    elif choix == 4:
        ventes = []
        nombre = int(input("Nombre de ventes : "))

        for i in range(nombre):
            vente = float(input("Montant de la vente : "))
            ventes.append(vente)

        resultat = calculer_total_ventes(ventes)
        print("Total des ventes :", resultat)

    elif choix == 5:
        print("Au revoir !")
        break

    else:
        print("Choix invalide")

    print()
