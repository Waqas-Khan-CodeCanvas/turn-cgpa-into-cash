import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

CSV_FILE = 'placement.csv'
MODEL_FILE = 'model.pkl'
SCALER_FILE = 'scaler.pkl'

app = Flask(__name__)

# ---------- helpers ----------
def train_and_persist():
    """Train model + scaler once, then re-use pickled files."""
    df = pd.read_csv(CSV_FILE)
    X = df[['cgpa']].values.astype(float)
    y = df['package'].values.astype(float)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    return model, scaler, df

def load_model():
    if os.path.exists(MODEL_FILE) and os.path.exists(SCALER_FILE):
        return joblib.load(MODEL_FILE), joblib.load(SCALER_FILE)
    return train_and_persist()[:2]

# ---------- routes ----------
@app.route('/')
def home():
    _, _, df = train_and_persist()          # ensure CSV is read once
    cgpa_list = df['cgpa'].tolist()
    package_list = df['package'].tolist()
    return render_template('index.html',
                           cgpa_list=cgpa_list,
                           package_list=package_list)

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.json['cgpa'])
    model, scaler = load_model()
    pred = model.predict(scaler.transform([[cgpa]]))[0]
    return jsonify({'package': round(float(pred), 2)})

# ===== university project pages =====
@app.route('/abstract')
def abstract():
    return render_template('abstract.html')

@app.route('/methodology')
def methodology():
    return render_template('methodology.html')

@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')
# ---------- entry ----------
if __name__ == '__main__':
    app.run(debug=True)


    