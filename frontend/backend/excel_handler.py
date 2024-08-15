import pandas as pd
import os

UPLOAD_DIRECTORY = "/frontend/uploads"

# Fonction pour obtenir les informations de l'utilisateur
def get_user_info(matricule: int):
    df1 = pd.read_excel(os.path.join(UPLOAD_DIRECTORY, 'fichier1.xlsx'))
    df2 = pd.read_excel(os.path.join(UPLOAD_DIRECTORY, 'fichier2.xlsx'))
    df3 = pd.read_excel(os.path.join(UPLOAD_DIRECTORY, 'fichier3.xlsx'))

    # Chercher les informations dans fichier 1
    user_info1 = df1[df1['matricule'] == matricule]
    if user_info1.empty:
        return None  # L'utilisateur n'existe pas dans fichier 1

    numero_affiliation = user_info1['numero_affiliation'].values[0]
    date_cotisation = user_info1['date_cotisation'].values[0]

    # Chercher les informations dans fichier 2
    user_info2 = df2[df2['matricule'] == matricule]
    nombre_mois = user_info2.shape[0]  # Nombre total de mois de cotisation

    # Chercher les informations dans fichier 3
    user_info3 = df3[df3['matricule'] == matricule]
    if user_info3.empty:
        a_avance = "Non"
    else:
        a_avance = user_info3['a_avance'].values[0]

    return {
        "numero_affiliation": numero_affiliation,
        "date_cotisation": date_cotisation,
        "nombre_mois": nombre_mois,
        "a_avance": a_avance
    }
