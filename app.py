import streamlit as st
import pandas as pd
st.write('ML Psy ! 🔥 ')

'''
# ML psy, aide au diagnostique psychiatrique
'''
df = pd.DataFrame({
    "Probabilité d'être malade": list(range(1, 11)),
    "Probabilité d'être sain": list(range(1, 11))
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Choix du nombre de maladies', 1, 7, 1)

# and used to select the displayed lines
head_df = df.head(line_count)
