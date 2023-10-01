import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st 
import pandas as pd 
import plotly

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


st.title("Application WEB")
st.write("AUTEUR : DJEGUI-WAGUE")





data=pd.DataFrame(data)


# Fonction d'analyse de données
def analyze_data(data):
    # Exemple d'analyse : Calcul de la somme des ventes par courtier
    total_ventes = data.groupby('Nom')['Ventes'].sum().reset_index()
    return total_ventes

# Convertir la colonne "Ventes" en nombres entiers


data['Ventes'] = data['Ventes'].str.replace(',', '').astype(int)


st.write(data)

# Analyser les données
st.write("Analyse des ventes par courtier :")
total_ventes = analyze_data(data)
st.write(total_ventes)

# Créer un graphique à barres avec Pandas
bar_chart = st.bar_chart(total_ventes.set_index('Nom'))

# Ajouter des couleurs personnalisées au graphique
bar_chart.plotly_chart({
    'data': [
        {
            'x': total_ventes['Nom'],
            'y': total_ventes['Ventes'],
            'type': 'bar',
            'marker': {'color': ['red', 'green', 'blue', 'yellow', 'purple','red', 'green', 'blue', 'yellow', 'purple','red', 'green', 'blue', 'yellow', 'purple','red', 'green', 'blue', 'yellow', 'purple','red', 'green', 'blue', 'yellow', 'purple','red']}  # Vous pouvez spécifier les couleurs ici
        }
    ],
    'layout': {
        'xaxis': {'title': 'Courtier'},
        'yaxis': {'title': 'Ventes'},
        'title': 'Ventes par courtier'
    }
})




# Sélection du courtier pour afficher les détails
selected_courtier = st.selectbox('Sélectionnez un courtier:', data['Nom'])

# Affichage des détails du courtier sélectionné
st.write('Détails du courtier sélectionné:')
selected_data = data[data['Nom'] == selected_courtier]
st.write(selected_data)





# Calculer les statistiques descriptives
statistics = data.describe()
st.write("Statistiques descriptives :")
st.write(statistics)


# Filtrer les données par critères spécifiques
st.write("Sous-ensemble de données :")
filter_criteria = st.slider("Ventes minimales", min_value=0, max_value=2000, value=0)
filtered_data = data[data['Ventes'] >= filter_criteria]
st.write(filtered_data)



data['Fiches'] = data['Fiches'].str.replace(',', '').astype(int)
# Curseur pour définir le nombre minimal de fiches
filter_fiches = st.slider("Fiches minimales", min_value=0, max_value=20, value=0)

# Filtrer les données en fonction des critères
filt_data = data[(data['Fiches']  <= filter_fiches)]

st.write(filt_data)






 

















