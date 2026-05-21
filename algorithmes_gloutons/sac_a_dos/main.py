def int_to_bin(n, nb):
    '''
    Entrées : n et nb sont de type int
    n est le nombre à convertir en binaire
    nb est le nombre de bits utilisés
    CU : l'algorithme utilisé est celui de la division euclidienne

    Sortie : la fonction retourne une chaîne
    de caractères contenant la représentation
    binaire de n
    '''
    
    ch = ""

    # Conversion en binaire par divisions successives
    while n > 0:
        r = n % 2
        n = n // 2
        ch = str(r) + ch

    # On complète éventuellement avec des zéros à gauche
    # pour former une chaîne de nb caractères
    ch = ch.zfill(nb)

    return ch

print(int_to_bin(150, 7))

def ens_des_parties(ensemble):
    """
    Entree : ensemble est une liste de p-uplets
    Sortie : une liste contenant toutes les parties de l'ensemble
    """

    # nombre d'éléments
    nb = len(ensemble)

    # nombre de parties
    n = 2 ** nb

    # ensemble des parties
    parties = []

    # former chaque partie puis l'ajouter à "parties"
    for i in range(1, n):
        ch = int_to_bin(i, nb)   # écriture de i sur nb bits
        partie = []

        for j in range(len(ch)):
            if ch[j] == "1":
                partie.append(ensemble[j])

        parties.append(partie)

    return parties