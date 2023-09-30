import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st 
import pandas as pd 
import matplotlib as plt 

def load_data():
    # Définissez les autorisations et l'accès au fichier JSON de clé d'API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("test-wague-9a205da3c6ca.json", scope)

    # Authentification avec les informations d'identification
    gc = gspread.authorize(credentials)

    # Ouvrir la feuille de calcul par son nom ou URL
    # Remplacez "Nom de votre feuille" par le nom de votre propre feuille ou l'URL
    worksheet = gc.open("courtier").sheet1

    # Lire les données de la feuille de calcul
    data = worksheet.get_all_values()

    # Convertir les données en un DataFrame pandas
    df = pd.DataFrame(data[1:], columns=data[0])

    return df

data = load_data()


st.title("Application de données Google Sheets avec Streamlit")




# Afficher les données dans une table
st.write("Données depuis Google Sheets :")
data=pd.DataFrame(data)


# Fonction d'analyse de données
def analyze_data(data):
    # Exemple d'analyse : Calcul de la somme des ventes par courtier
    total_ventes = data.groupby('Nom')['Ventes'].sum().reset_index()
    return total_ventes

# Convertir la colonne "Ventes" en nombres entiers


data['Ventes'] = data['Ventes'].str.replace(',', '').astype(int)

# Afficher les données dans une table
st.write("Données depuis Google Sheets :")
st.write(data)

# Analyser les données
st.write("Analyse des ventes par courtier :")
total_ventes = analyze_data(data)
st.write(total_ventes)

# Créer un graphique à barres avec Pandas
st.bar_chart(total_ventes.set_index('Nom'))


# Calculer les statistiques descriptives
statistics = data.describe()
st.write("Statistiques descriptives :")
st.write(statistics)


# Filtrer les données par critères spécifiques
st.write("Sous-ensemble de données :")
filter_criteria = st.slider("Ventes minimales", min_value=0, max_value=2000, value=0)
filtered_data = data[data['Ventes'] >= filter_criteria]
st.write(filtered_data)



# Sélectionner les colonnes "Nom" et "Ventes" et les convertir en dictionnaire
data_dict = data[['Nom', 'Ventes']].to_dict(orient='records')

# Afficher le dictionnaire
st.write("Dictionnaire avec les colonnes 'Nom' et 'Ventes' :")
# Création d'un DataFrame à partir des données
df = pd.DataFrame(data_dict)
st.write(df)



 # Créer un graphique à barres avec Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Ventes', y='Nom', data=data, palette='viridis')
ax.set_xlabel("Nombre de ventes")
ax.set_ylabel('Nom')
ax.set_title("Nombre de ventes par nom")

st.pyplot()

















