import streamlit as st
import pandas as pd
import requests
import json

# st.write('ML Psy ! 🔥 ')

'''
# ML psy, aide au diagnostique psychiatrique
'''

df_sample = pd.read_csv("data_preprocessed_test_data_main_dataset_X_preprocessed.csv")
df_results = pd.DataFrame({
    "Pathologie": ["valeur 1", "valeur 2", "valeur 3"]
})

name_to_value = {
    "Bob": 1,
    "James": 2,
    "Alice": 3,
    "Emma": 4
}

st.write("")
params = name_to_value[st.selectbox("Choisir un patient:", list(name_to_value))]
# st.write(params)
st.write("")

# if st.button("Predire un diagnostic"):
#      st.write('100% Schizo')

button = st.button("Predire un diagnostic")
if st.button("Predire un diagnostic"):
    print('go')
    api_url = "https://ml-psy-api-b6cjkk5ioq-ew.a.run.app/predict"
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        # st.write(f"Prediction: {prediction}")
        # st.dataframe(json.loads(prediction)).head(7)
        st.write("")
        st.write("Résultats")
        st.dataframe(df_results.head())
    else:
        st.write("Error: Could not retrieve prediction")

# st.dataframe(df_sample.head())
# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
# line_count = st.slider('Choix du nombre de maladies', 1, 7, 1)

# and used to select the displayed lines
# head_df = df.head(line_count)

# params = head_df

