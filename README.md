# 🏠 ML Model Deployment with FastAPI & Docker

A production-ready REST API that serves a Machine Learning model for predicting California housing prices, containerized with Docker.

## 🚀 Tech Stack

- **Scikit-learn** — GradientBoostingRegressor model
- **FastAPI** — REST API with automatic documentation
- **Docker** — Containerization for consistent deployment
- **Pydantic** — Data validation

## 📊 Model

Trained on the California Housing dataset using Gradient Boosting Regressor with:
- 100 estimators
- Learning rate: 0.1
- Max depth: 3

## ▶️ Run with Docker

```bash
docker build -t ml-housing-api .
docker run -d -p 8081:80 --name housing-container ml-housing-api
```

Open http://localhost:8081/docs for the interactive API documentation.

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Predict housing price |

## 📥 Example Request

```json
{
  "MedInc": 3.5,
  "HouseAge": 20.0,
  "AveRooms": 5.0,
  "AveBedrms": 1.0,
  "Population": 800.0,
  "AveOccup": 3.0,
  "Latitude": 34.0,
  "Longitude": -118.0
}
```

## 📤 Example Response

```json
{
  "predicted_median_value": "$179213.89"
}
```
## 🌐 Live Demo
👉 https://ml-docker-housing.onrender.com/docs