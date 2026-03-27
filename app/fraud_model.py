import joblib
import pandas as pd

from app.config import MODEL_PATH


class FraudModel:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict_proba(self, transaction_data: dict) -> float:
        input_df = pd.DataFrame([transaction_data])
        fraud_prob = self.model.predict_proba(input_df)[:, 1][0]
        return float(fraud_prob)