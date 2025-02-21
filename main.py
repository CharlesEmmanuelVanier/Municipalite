import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#On lit le fichier csv
df = pd.read_csv('Census_2016_2021.csv', delimiter = ',', decimal ='.')
#On crée un dataframe avec seulement les municipalité
df_me = df[df['Type'] == 'MÉ'].reset_index(drop=True)

#La grosseur du dataframe est le nombre de municipalité dans le dataframe
print(f"Il y a {len(df_me)} municipalité de listé dans ce fichier\n")

#Calcul et affichage des moyennes de populations selon l'année du recensement
moyenne_2016 = df_me["Pop16"].mean()
moyenne_2021 = df_me["Pop21"].mean()

print(f"Moyenne pop 2016 : {moyenne_2016}")
print(f"Moyenne pop 2021 : {moyenne_2021}")

#Graphique d'accroissement de population entre l'année 2016 et 2021
plt.plot(df_me["Pop21"], ((df_me["Pop21"]-df_me["Pop16"])/df_me["Pop16"])*100 ,"ob")
plt.xlabel("Population en 2021")
plt.ylabel("Ratio d'accroissement de la population entre 2016 et 2021")
plt.show()

#Création des catégories de population
df_cat1 = df_me[df_me["Pop21"] < 1999]
df_cat2 = df_me[(df_me["Pop21"] > 2000) & (df_me["Pop21"] < 9999)]
df_cat3 = df_me[(df_me["Pop21"] > 10000) & (df_me["Pop21"] < 24999)]
df_cat4 = df_me[(df_me["Pop21"] > 25000) & (df_me["Pop21"] < 99999)]
df_cat5 = df_me[df_me["Pop21"] > 100000]

#Création d'une liste avec le nombre de municipalité dans chaque catégories puis un graphique
pop_list = [df_cat1["Pop21"].count(), df_cat2["Pop21"].count(),df_cat3["Pop21"].count(),df_cat4["Pop21"].count(),df_cat5["Pop21"].count()]

plt.bar(["pop<1999","2000<pop<9999","10000<pop<24999","25000<pop<99999","100000<pop"], pop_list,label="True")
plt.show()