# Calcul de la marge commerciale
def calculer_marge(vente, achat):
    marge = vente - achat
    taux_marge = (marge / achat) * 100 if achat != 0 else 0
    taux_marque = (marge / vente) * 100 if vente != 0 else 0
    return marge, taux_marge, taux_marque
