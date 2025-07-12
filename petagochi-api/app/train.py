import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os

# Load and preprocess your data
data = pd.read_csv("interactions.csv")  # Or wherever your training data is

X = data[["hunger", "energy", "mood", "last_action"]]
y = data["pet_state"]

# Encode categorical columns
action_encoder = LabelEncoder()
X["last_action"] = action_encoder.fit_transform(X["last_action"])

state_encoder = LabelEncoder()
y_encoded = state_encoder.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Start MLflow experiment
mlflow.set_tracking_uri("/Users/gupalo/Documents/mlops/petagochi-api/mlruns")  # local folder in colab or change if using server
mlflow.set_experiment("Petagotchi ML Experiment")

with mlflow.start_run():
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log metrics and model
    mlflow.log_metric("accuracy", acc)
    mlflow.log_param("model_type", "LogisticRegression")

    # Save and log the model
    os.makedirs("model", exist_ok=True)
    model_path = "model/model.pkl"
    joblib.dump(model, model_path)
    mlflow.sklearn.log_model(model, "petagotchi_model")

    # Save and log encoders too
    joblib.dump(action_encoder, "model/action_encoder.pkl")
    joblib.dump(state_encoder, "model/state_encoder.pkl")
    mlflow.log_artifact("model/model.pkl")
    mlflow.log_artifact("model/action_encoder.pkl")
    mlflow.log_artifact("model/state_encoder.pkl")

print(f"Model trained and tracked with accuracy: {acc:.3f}")
