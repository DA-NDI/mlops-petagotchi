from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Load artifacts
model = joblib.load("model.pkl")
action_encoder = joblib.load("action_encoder.pkl")
state_encoder = joblib.load("state_encoder.pkl")

app = FastAPI(title="Petagotchi Model API")

# Input format
class InputData(BaseModel):
    last_action: str
    energy: float
    hunger: float
    mood: float

@app.get("/")
def home():
    return {"message": "Petagotchi Inference API is running"}

@app.post("/predict")
def predict(data: InputData):
    try:
        df = pd.DataFrame([data.dict()])
        df["last_action"] = action_encoder.transform(df["last_action"])
        pred = model.predict(df)
        result = state_encoder.inverse_transform(pred)
        return {"predicted_state": result[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
