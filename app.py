import streamlit as st
import pandas as pd
import requests
import json
import ast

'''
# Welcome to ML Psy !  :brain:
## Your AI-powered psych diagnosis assistant
'''

name_to_value = {
    "John" : 0,
    "Bob": 1,
    "James": 2,
    "Alice": 3,
    "Emma": 4,
    "Aline" : 5,
    "Marin" : 17
}

# Champs de saisie pour l'utilisateur
index = name_to_value[st.selectbox("Choose a patient:", list(name_to_value))] #st.text_input("Entrez l'index:", list(name_to_value))
#threshold = st.number_input("Entrez le seuil (threshold):", min_value=0.0, step=0.1)

# URL de l'API (à modifier selon votre API)
api_url = "http://127.0.0.1:8000/predict"

# Bouton pour soumettre les paramètres
if st.button("Diagnose"):
    # Vérification que les deux champs ne sont pas vides
    if index is not None:
        # Préparation des paramètres pour l'appel API
        params = {
            'patient': str(index),
            'threshold': str(0)
        }

        # Requête à l'API
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Vérifie que la requête est réussie

            # Récupération et traitement de la réponse de l'API
            data = response.json()
            data = ast.literal_eval(data)

            # Conversion de la réponse en liste de tuples (clé, valeur) et tri par valeur décroissante
            sorted_data = sorted(data.items(), key=lambda item: float(item[1]), reverse=True)
            print(sorted_data)

            # Affichage de la réponse triée

            #st.write(f"### ML Psy advises you to explore a diagnosis of **{sorted_data[0][0]}** {sorted_data[0][1]} and **{sorted_data[1][0]}**")

            #for disorder, probability in sorted_data[0]:
            if float(sorted_data[0][1]) < 0.5 :
                st.write(f"### The patient is healthy")
            else :
                st.write(f"### ML Psy advises you to explore a diagnosis of **{sorted_data[0][0]}**")



        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de l'appel à l'API : {e}")
    else:
        st.warning("Veuillez entrer un index valide et un seuil (threshold).")
