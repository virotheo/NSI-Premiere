def tri_selection(tab):
    for i in range((len(tab)-1)):
        min=i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min=j
        tab[i],tab[min]=tab[min],tab[i]
    return tab

def tri_insertion(tab):
    n=len(tab)
    
    for j in range(1,n):
        cle=tab[j]
        k=j-1
        while k>=0 and tab[k]>cle:
            tab[k+1]=tab[k]
            k=k-1
        tab[k+1]=cle
    return tab

def tri_a_bulles(tab):
    i=len(tab)-1  #indice du dernier Ã©lÃ©ment du tableau

    while i>=0:
        for j in range(i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
        i=i-1
    return tab
    
############################################"

def fusion(T1,T2):
    '''
    Entree : deux listes T1 et T2 ordonnÃ©es dans le
    sens croissant

    Sortie: une liste rÃ©sultat de la fusion de T1 et de T2
    '''
    T=[0]*(len(T1)+len(T2))
    i1=i2=j=0

    while i1 < len(T1) and i2< len(T2):
        if T1[i1]<T2[i2]:
            T[j]=T1[i1]
            i1+=1
        else:
            T[j]=T2[i2]
            i2+=1
        j+=1
    
    while i1<len(T1):
        T[j]=T1[i1]
        i1+=1
        j+=1
    while i2 < len(T2):
        T[j]=T2[i2]
        i2+=1
        j+=1
    return T

def tri_fusion(T):
    n=len(T)
    #si la liste est vide ou contient 1 seul Ã©lÃ©ment
    if n<2:
        return T[:] #on renvoie une copie de la liste
    
    T1=T[0 : n//2]
    T2=T[n//2:n]

    T1=tri_fusion(T1)
    T2=tri_fusion(T2)
    return fusion(T1,T2)








