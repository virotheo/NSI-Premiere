import pandas
from statistics import mean
radiations= pandas.read_csv("radiations.csv", delimiter = ";", keep_default_na=False) # Lire le fichier csv
# #1
print(radiations[radiations.Departement == 'Paris']['commune'].unique())
# #2
print(radiations[radiations.Departement == 'Paris'][['EnSolAn' ,'commune']])
#3
print(radiations[radiations['Climat'] == 'Méditerranéen'][['commune', 'EnSolAn']].nlargest(10, 'EnSolAn'))
#4
print(radiations[['commune', 'EnSolAn']].nsmallest(10, 'EnSolAn'))
#5
print(radiations[radiations.commune == 'Rueil-Malmaison']['EnSolAn'].unique())
#6
print(radiations[['commune','Departement' , 'TempAnMoy']].nsmallest(10, 'TempAnMoy'))
#7
print(radiations[['commune','Departement' , 'TempAnMoy']].nlargest(10, 'TempAnMoy'))

# Question Bonus : Afficher la moyenne des temperatures moyennes des régions Hauts-de-France puis PACA
print(radiations[radiations.Region == 'Hauts-de-France']['TempAnMoy'].mean())
print(radiations[radiations.Region == "Provence-Alpes-Côte d'Azur"]['TempAnMoy'].mean())
