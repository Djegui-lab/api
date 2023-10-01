
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st 
import pandas as pd 



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

st.title("Application WEB")
st.write("AUTEUR : DJEGUI-WAGUE")



# Dictionnaire pour stocker les informations de l'utilisateur
utilisateur = {
    'Nom': ' WAGUE',
    'Prénom': 'DJEGUI',
    'Âge': '26',
    'Adresse e-mail': 'dwague44@gmail.com',
    'Numéro': '+212605275874'
}

# Mot de passe pour accéder à la fonctionnalité
mot_de_passe_valide = "djegui0000"

# Vérifiez le mot de passe pour accéder aux informations
st.title("Accédez aux Informations")
mot_de_passe = st.text_input("Entrez votre mot de passe pour accéder aux informations :", type="password")

if mot_de_passe == mot_de_passe_valide:
    st.success("Mot de passe correct ! Vous avez accès aux informations.")
    data = load_data()
    df=pd.DataFrame(data)
    st.subheader("base de données courtier(ASSURANCE)")
    st.write(df)

    # Affichez les informations de l'utilisateur
    st.write("Informations de l'utilisateur :")
    for cle, valeur in utilisateur.items():
        st.write(f"{cle}: {valeur}")
     
else:
    # Si le mot de passe est incorrect, affichez un message d'erreur
    st.error("Mot de passe incorrect. Vous n'avez pas accès aux informations.")



demander_nom=st.text_input("QUEL EST VOTRE NOM ?")
button = st.button("Valider")
if button:
   st.write("Bonjour",demander_nom, "je suis un model fabriqué par:Djégui-Wagué")
else: 
    st.write("veuillez entrer votre nom")




data = load_data()





# Fonction d'analyse de données
def analyze_data(data):
    # Exemple d'analyse : Calcul de la somme des ventes par courtier
    total_ventes = data.groupby('Nom')['Ventes'].sum().reset_index()
    return total_ventes

# Convertir la colonne "Ventes" en nombres entiers


data['Ventes'] = data['Ventes'].str.replace(',', '').astype(int)



# Analyser les données

print()
print()
st.write("Analyse des ventes par courtier :")
total_ventes = analyze_data(data)
#st.write(total_ventes)

st.bar_chart(total_ventes.set_index('Nom'))





# Sélection du courtier pour afficher les détails
selected_courtier = st.selectbox('Sélectionnez un courtier:', data['Nom'])

# Affichage des détails du courtier sélectionné
st.write('Détails du courtier sélectionné:')
selected_data = data[data['Nom'] == selected_courtier]
st.write(selected_data)





# Calculer les statistiques descriptives
st.subheader("Statistiques descriptives :")

statistics = data.describe()
st.write(statistics)


# Filtrer les données par critères spécifiques
st.subheader("TRIER LES DONNÉES PAR VENTE :")
filter_criteria = st.slider("Ventes minimales", min_value=0, max_value=2000, value=0)
filtered_data = data[data['Ventes'] >= filter_criteria]
st.write(filtered_data)



data['Fiches'] = data['Fiches'].str.replace(',', '').astype(int)
# Curseur pour définir le nombre minimal de fiches
st.subheader("TRIER LES DONNÉES PAR FICHE :")

filter_fiches = st.slider("Fiches minimales", min_value=0, max_value=20, value=0)

# Filtrer les données en fonction des critères
filt_data = data[(data['Fiches']  <= filter_fiches)]

st.write(filt_data)
st.write()
st.write()
mot_de_passe_correct = "djegui0000"

# Affichez un champ de saisie de mot de passe
mot_de_passe_utilisateur = st.text_input("Veuillez entrer le mot de passe", type="password")

# Vérifiez si le mot de passe est correct lorsque l'utilisateur soumet le formulaire
if st.button("Se connecter"):
    if mot_de_passe_utilisateur == mot_de_passe_correct:
        # Redirigez l'utilisateur vers l'autre application en fonction de l'URL
        lien_autre_app = "https://djegui-hello-bgctyuzfiydk2zkbzmyzna.streamlit.app/"
        st.write("Mot de passe correct. Vous pouvez accéder à l'application [ici](%s)." % lien_autre_app)
    else:
        st.write("Mot de passe incorrect. Veuillez réessayer.")





 

















