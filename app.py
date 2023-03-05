import streamlit as st
import pandas as pd
import pickle

st.header("Кардио APP")
st.subheader("Введите данные и узнайте вероятность проблем с сердцем")

def load():
    with open("C:/Users/Alexander Malfington/model2.pcl", "rb") as fid:
        return pickle.load(fid)

age = st.slider('Возраст', 25, 65)
gender = st.radio('Пол', (0, 1))
height = st.slider('Рост', 80, 200)
weight = st.slider('Вес', 40, 120)
ap_hi = st.slider('Верхнее давление', 80, 200)
ap_lo = st.slider('Нижнее давление', 40, 120)
cholesterol = st.radio('Холестерин', (1, 2, 3))
gluc = st.radio('Глюкоза', (1, 2, 3))
smoke = st.radio('Курение', (0, 1))
alco = st.radio('Алкоголь', (0, 1))
active = st.radio('Активный образ жизни', (0, 1))

model = load()

y_pr = model.predict_proba(pd.DataFrame([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]], columns=['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']))[:, 1]

st.write(y_pr)