# model.py

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import fetch_california_housing
import joblib

def train_and_save_model():
    print("Cargando datos y entrenando el modelo...")

    housing = fetch_california_housing()
    X, y = housing.data, housing.target

    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
    model.fit(X, y)

    joblib.dump(model, 'housing_model.pkl')

    print("✅ Modelo entrenado y guardado como housing_model.pkl")
    print("Features:", housing.feature_names)

if __name__ == "__main__":
    train_and_save_model()