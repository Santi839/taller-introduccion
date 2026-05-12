import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load('modelo_desercion.pkl')

st.title('Predicción de Deserción Estudiantil')
st.write('Ingrese los datos del estudiante para predecir el riesgo de deserción.')

# Formulario de entrada
edad = st.number_input('Edad', min_value=15, max_value=60, value=20)
promedio = st.slider('Promedio Acumulado', 0.0, 5.0, 3.5)
materias_reprobadas = st.number_input('Materias Reprobadas', 0, 50, 0)
ingresos = st.number_input('Ingresos Familiares (SMLV)', 0.0, 50.0, 2.0)
horas_estudio = st.slider('Horas de Estudio Semanal', 0, 100, 20)
apoyo = st.selectbox('¿Cuenta con apoyo económico?', ['No', 'Sí'])

# Convertir apoyo a numérico
apoyo_num = 1 if apoyo == 'Sí' else 0

# Botón de predicción
if st.button('Predecir'):
    features = np.array([[edad, promedio, materias_reprobadas, ingresos, horas_estudio, apoyo_num]])
    prediccion = modelo.predict(features)
    
    if prediccion[0] == 1:
        st.error('El estudiante tiene un alto riesgo de deserción.')
    else:
        st.success('El estudiante tiene un bajo riesgo de deserción.')
