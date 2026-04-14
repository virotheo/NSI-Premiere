from listes import * 
from tris import *
from timeit import timeit
import pylab

print("Veuillez patienter le graphique est en train de se générer...")

'''
print(timeit(setup='from tris import tri_selection; from listes import cree_liste_melangee',
stmt='tri_selection(cree_liste_melangee(2000))',
number=300))

print(timeit(setup='from tris import tri_a_bulles; from listes import cree_liste_melangee',
stmt='tri_a_bulles(cree_liste_melangee(2000))',
number=300))

print(timeit(setup='from tris import tri_fusion; from listes import cree_liste_melangee',
stmt='tri_fusion(cree_liste_melangee(2000))',
number=300))
''''''

def temps_de_tri(tri,taille_liste,nb_essais):
    return timeit(setup=f"'from tris import {tri}; from listes import cree_liste_melangee'",
    stmt=f"'{tri}(cree_liste_melangee({taille_liste}))'",
    number=nb_essais)


'''
def temps_de_tri(tri, taille_liste, nb_essais):
    return timeit(
        setup=f"from tris import {tri}; from listes import cree_liste_melangee",
        stmt=f"{tri}(cree_liste_melangee({taille_liste}))",
        number=nb_essais
    )

import time

def temps_de_tri_interm(tri,i,nombre_essais):
    temps = []
    
    for i in range(1, i + 1):
        chaine = f"tri_selection(cree_liste_decroissante({i}))"
        temps.append(temps_de_tri(tri,i,nombre_essais))
    return temps    
        
def courbe(tri,taille_max,nb_essais):
    liste = temps_de_tri_interm(tri,taille_max,nb_essais)
    pylab.plot(liste)
    pylab.show()

def toutes_courbes(taille_max,nb_essais):
    liste1 = temps_de_tri_interm('tri_selection',taille_max,nb_essais)
    liste2 = temps_de_tri_interm('tri_a_bulles',taille_max,nb_essais)
    liste3 = temps_de_tri_interm('tri_insertion',taille_max,nb_essais)
    liste4 = temps_de_tri_interm('tri_fusion',taille_max,nb_essais)
    pylab.plot(liste1,label='selection')
    pylab.plot(liste2,label='bulles')
    pylab.plot(liste3,label='insertion')
    pylab.plot(liste4,label='fusion')
    pylab.grid()
    pylab.legend()
    pylab.show()

toutes_courbes(200,100)  
'''print(temps_de_tri_interm('tri_a_bulles',100,1))'''
'''
liste_1 = temps_de_tri('tri_a_bulles',100,100)
liste_2 = temps_de_tri('tri_fusion',100,100)
liste_3 = temps_de_tri('tri_selection',100,100)
liste_4 = temps_de_tri('tri_insertion',100,100)
pylab.plot(liste_1, label='bulle')
pylab.plot(liste_2, label='fusion')
pylab.plot(liste_3, label='selection')
pylab.plot(liste_4, label='insertion')
pylab.legend(loc='upper left')
NBRE_ESSAIS = 100
pylab.title('Temps du tri par sélection (pour {:d} essais)'.format(NBRE_ESSAIS))
pylab.xlabel('taille des listes')
pylab.ylabel('temps en secondes')
pylab.grid()
'''