from random import *
import matplotlib.pyplot as plt

debut = 0
fin = 8
duree_max = 5
NOMBRE_INTERVALLES = 10

def intervalles(nb_intervalles):
    tab_intervalles = []
    for i in range(nb_intervalles):
        duree = randint(1, duree_max)
        deb = randint(debut, fin - duree)
        tab_intervalles.append([deb, deb + duree, 'C ' + str(i)])
    print(tab_intervalles)
    return tab_intervalles

def planning(tab_intervalles):
    nb_intervalles = len(tab_intervalles)

    # tri par heure de fin croissante (indice 1 de chaque intervalle)
    tab_intervalles = sorted(tab_intervalles, key=lambda x: x[1])

    # on initialise le planning avec le 1er conferencier (celui qui finit le plus tot)
    tab_planning = [tab_intervalles[0]]

    j = 0  # j = indice du dernier conferencier accepte dans le planning

    for i in range(1, nb_intervalles):

        # condition de compatibilite : i commence apres la fin du dernier accepte (j)
        if tab_intervalles[i][0] >= tab_intervalles[j][1]:

            # les deux intervalles sont compatibles, on accepte i
            tab_planning.append(tab_intervalles[i])
            j = i

    return tab_planning

def affichage():
    conferenciers = planning(intervalles(NOMBRE_INTERVALLES))

    for i in range(len(conferenciers)):
        Y = [i + 1, i + 1]
        a = (conferenciers[i][0] + conferenciers[i][1]) / 2
        texte = conferenciers[i][2]
        plt.plot(conferenciers[i][:2], Y, linestyle='solid',
                 marker='o', color='red', markersize=2)
        plt.annotate(texte, xy=(a, float(i + 1) + 0.2))
    plt.axis([0, fin + 2, 0, fin + 2])
    plt.show()

affichage()