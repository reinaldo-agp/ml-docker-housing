# main.py

from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Predictor de Precios de Casas en California")

model = joblib.load('housing_model.pkl')

class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict", tags=["Predicciones"])
async def predict_price(features: HousingFeatures):
    data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])
    prediction = model.predict(data)[0]
    return {"predicted_median_value": f"${prediction * 100000:.2f}"}

@app.get("/", tags=["General"])
async def read_root():
    return {"message": "API de predicción de precios funcionando ✅"}