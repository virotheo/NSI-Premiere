# Script 1 
'''
def rendu_monnaie(systeme_monnaie, somme_a_rendre):
    results = []
    for piece in systeme_monnaie:
      while somme_a_rendre >= piece:
            somme_a_rendre -= piece
            results.append(piece)
    return results        
'''

# Script optimisé

def rendu_monnaie(systeme_monnaie, somme_a_rendre):
    results = []
    i = 0  
    while somme_a_rendre > 0 and i < len(systeme_monnaie):
        if somme_a_rendre >= systeme_monnaie[i]:
            somme_a_rendre -= systeme_monnaie[i]
            results.append(systeme_monnaie[i])
        else:
            i += 1  
    return results

# Exemples :     

print(rendu_monnaie([50,20,10,5,2,1],49))            
print(rendu_monnaie([50,20,10],30))            
print(rendu_monnaie([50,20,2,1],93))            
