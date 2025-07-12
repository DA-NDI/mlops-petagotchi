from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load model and encoders
model_path = os.path.join("app", "model")
model = joblib.load(os.path.join(model_path, "model.pkl"))
le_action = joblib.load(os.path.join(model_path, "action_encoder.pkl"))
le_state = joblib.load(os.path.join(model_path, "state_encoder.pkl"))

# Input schema
class Interaction(BaseModel):
    hunger: float
    energy: float
    mood: float
    last_action: str

@app.get("/")
def home():
    return {"message": "Petagotchi ML API is running"}

@app.post("/predict")
def predict(data: Interaction):
    try:
        action_encoded = le_action.transform([data.last_action])[0]
    except:
        return {"error": f"Unknown action: {data.last_action}"}

    input_data = [[data.hunger, data.energy, data.mood, action_encoded]]
    prediction = model.predict(input_data)
    predicted_state = le_state.inverse_transform(prediction)[0]
    return {"predicted_pet_state": predicted_state}
