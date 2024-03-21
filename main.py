
import pandas as pd
#code de connexion  a la base de donné
import mysql.connector
from mysql.connector import Error

# Chemin vers votre fichier CSV
raisin_base = pd.read_excel("Raisin_Dataset.xlsx")
print(raisin_base)
print(raisin_base.columns)

#colonnes = ['area','major_axis_length','']

# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_raisin"
    )
    #if conn.is_connected():
       # print("La connexion à MySQL est reussi.")
      
except Error as e:
    print("Erreur lors de la connexion à MySQL :", e)







