import csv
plantes = []
with open('fleurs.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    for row in spamreader:
        plantes.append(dict(row))

# 2
#print(set([p['commune']for p in plantes]))
#3
#print(set([p['nom_fr']for p in plantes if p['commune'] == 'CHATENAY MALABRY']))
#4
#print(set([p['nom_fr']for p in plantes if p['code_insee'] == '92060']))
#5
#print(set([p['nom_fr']for p in plantes if p['date_obs'] < '1995-01-01']))
#6

#taille de ensemble plantes
# ensemble_plantes= set([p['nom_fr']for p in plantes if p['code_insee'] == '92060'])
# print(len(ensemble_plantes))
#6
#print(sorted([(p['nom_fr'], p['date_obs']) for p in plantes if p['commune'] == 'CHATENAY MALABRY'],key=lambda x: x[1]))

#7
#print(sorted([(p['commune'], p['date_obs']) for p in plantes if p['nom_fr'] == 'Trèfle des près'],key=lambda x: x[0]))
