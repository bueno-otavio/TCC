# === app.py (Flask) ===
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

app = Flask(__name__)

model_path = 'E_WL_model.keras'

if not os.path.exists(model_path):
    raise FileNotFoundError("Modelo E_WL_model.keras não encontrado.")

model = load_model(model_path)

# Novo scaler baseado apenas em queue_length (faixa fictícia 0 a 20)
scaler = MinMaxScaler()
scaler.fit([[0], [20]])

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get("sequence")  # 10 valores

    if not sequence or len(sequence) != 10:
        return jsonify({"error": "Sequência incompleta ou ausente"}), 400

    seq_array = np.array(sequence).reshape(10, 1)
    seq_scaled = scaler.transform(seq_array).reshape(1, 10, 1)

    prediction = model.predict(seq_scaled, verbose=0)
    predicted_scaled = float(prediction[0][0])
    predicted = scaler.inverse_transform([[predicted_scaled]])[0][0]

    return jsonify({"predicted_queue_length": predicted})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
