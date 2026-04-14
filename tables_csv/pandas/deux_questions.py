import pandas
radiations= pandas.read_csv("radiations.csv", delimiter = ";", keep_default_na=False) # Lire le fichier csv
#Question 1 : Afficher les communes avec un climat Montagnard et leur température moyenne annuelle, triées par température décroissante
print(radiations[radiations.Climat == 'Montagnard'][['commune', 'TempAnMoy']].nlargest(10, 'TempAnMoy'))
#Question 2 : Afficher les 10 communes de plus de 100 000 habitants les moins ensoleillées par an
print(radiations[radiations.Population > 100000][['commune', 'Population', 'EnSolAn']].nsmallest(10, 'EnSolAn'))