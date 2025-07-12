import argparse
import os
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

parser = argparse.ArgumentParser()
parser.add_argument("--output-data-dir", type=str, default="/opt/ml/output/data")  
parser.add_argument("--model-dir", type=str, default="/opt/ml/model")              
parser.add_argument("--data-dir", type=str, default="/opt/ml/input/data/training") 
args = parser.parse_args()

data_path = os.path.join(args.data_dir, "interactions.csv")
data = pd.read_csv(data_path)

X = data[["hunger", "energy", "mood", "last_action"]]
y = data["pet_state"]

action_encoder = LabelEncoder()
X["last_action"] = action_encoder.fit_transform(X["last_action"])

state_encoder = LabelEncoder()
y_encoded = state_encoder.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

mlflow.set_tracking_uri("file:/opt/ml/model/mlruns")  # change from local
mlflow.set_experiment("Petagotchi ML Experiment")

with mlflow.start_run():
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_metric("accuracy", acc)
    mlflow.log_param("model_type", "LogisticRegression")

    os.makedirs(args.model_dir, exist_ok=True)

    model_path = os.path.join(args.model_dir, "model.pkl")
    joblib.dump(model, model_path)

    joblib.dump(action_encoder, os.path.join(args.model_dir, "action_encoder.pkl"))
    joblib.dump(state_encoder, os.path.join(args.model_dir, "state_encoder.pkl"))

    # Log artifacts (optional - todo)
    #mlflow.log_artifact(model_path)
    #mlflow.log_artifact(os.path.join(args.model_dir, "action_encoder.pkl"))
    #mlflow.log_artifact(os.path.join(args.model_dir, "state_encoder.pkl"))

print(f"Model trained and tracked with accuracy: {acc:.3f}")
