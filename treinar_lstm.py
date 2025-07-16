import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# === 1. Caminho do CSV ===
csv_path = os.path.join("data", "traffic_data.csv")
if not os.path.exists(csv_path):
    raise FileNotFoundError("Arquivo traffic_data.csv não encontrado na pasta 'data'.")
df = pd.read_csv(csv_path)

# === 2. Filtrar apenas E_WL e a coluna de interesse ===
df = df[df['edge_id'] == 'E_WL']
df['time_bin'] = (df['timestamp'] // 5) * 5

df = df[['edge_id', 'time_bin', 'queue_length']]
df.fillna(0, inplace=True)

# === 3. Agregar por faixa de tempo ===
df_grouped = df.groupby(['edge_id', 'time_bin']).agg({
    'queue_length': 'mean'
}).reset_index()

# === 4. Preparar dados com apenas queue_length ===
def preparar_dados(df_grouped, edge):
    df_edge = df_grouped[df_grouped['edge_id'] == edge].copy()
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df_edge[['queue_length']])
    df_scaled = pd.DataFrame(scaled, columns=['queue_length'])

    X, y = [], []
    for i in range(len(df_scaled) - 10):
        X.append(df_scaled.iloc[i:i+10].values)
        y.append(df_scaled.iloc[i+10]['queue_length'])

    return np.array(X), np.array(y), scaler

# === 5. Construir e treinar modelo ===
def build_model(X, y, name):
    model = Sequential()
    model.add(LSTM(32, input_shape=(X.shape[1], X.shape[2]), activation='tanh'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=30, batch_size=16, verbose=1)
    model.save(f"{name}_model.keras")
    print(f"✅ Modelo {name} salvo como {name}_model.keras")

# === 6. Treinar somente E_WL ===
X, y, scaler = preparar_dados(df_grouped, 'E_WL')
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
build_model(X_train, y_train, "E_WL")
