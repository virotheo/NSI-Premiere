import pandas

# Introduction à la lib Pandas
fleurs= pandas.read_csv("fleurs.csv", delimiter = ";", keep_default_na=False) # Lire le fichier csv
print(fleurs.head) # Affiche les premières rentrées de la table
print(fleurs.sample(7)) # Affiche 7 enregistrements au hasard
print(fleurs.describe())
print(fleurs.dtypes) # Afficher les noms des différentes colonnes
print(fleurs['nom_fr'])

# Réponses aux questions du pdf sur fleurs.csv

print(fleurs['commune'].unique()) #2
print(fleurs[fleurs.commune == 'CHATENAY MALABRY']['nom_fr'].unique()) #3
print(fleurs[fleurs.code_insee == '92060']['nom_fr'].unique()) #4
print(fleurs[fleurs.date_obs < '1995-01-01'][['nom_fr' , 'date_obs']]) #5
resultat = fleurs[fleurs.commune == 'CHATENAY MALABRY'][['nom_fr' , 'date_obs']]
print(resultat.sort_values(by='date_obs',ascending=False)) #6
resultat = fleurs[fleurs.nom_fr == 'Trèfle des près'][['commune' , 'date_obs']]
print(resultat.sort_values(by=['commune','date_obs'],ascending=[True,False])) #7
