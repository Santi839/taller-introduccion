from flask import Flask, request, jsonify, send_from_directory
import sys
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('modelo_desercion.pkl')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json(force=True)

    features = np.array([[
        payload.get('edad', 20),
        payload.get('promedio', 3.5),
        payload.get('materias_reprobadas', 0),
        payload.get('ingresos', 2.0),
        payload.get('horas_estudio', 20),
        payload.get('apoyo', 0)
    ]], dtype=float)

    prediction = model.predict(features)
    risk = 'alto' if int(prediction[0]) == 1 else 'bajo'
    message = (
        'El estudiante tiene un alto riesgo de deserción.'
        if risk == 'alto'
        else 'El estudiante tiene un bajo riesgo de deserción.'
    )

    return jsonify({
        'risk': risk,
        'message': message
    })

if __name__ == '__main__':
    # Si el script es ejecutado por Streamlit, Streamlit ya ejecuta en
    # su propio runner (no en el hilo principal), por lo que iniciar
    # el servidor de desarrollo de Flask provoca errores con `signal`.
    # Evitamos arrancar el servidor cuando `streamlit` está cargado.
    if 'streamlit' in sys.modules:
        # No iniciar Flask aquí; ejecutar el servidor Flask por separado.
        pass
    else:
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
