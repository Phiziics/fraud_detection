import json
from pathlib import Path

import joblib
import pandas as pd

from app.config import MODEL_PATH, METADATA_PATH


class FraudModel:
    def __init__(self):
        self.model = None
        self.metadata = None
        self.expected_features = None
        self.load()

    def load(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

        if not METADATA_PATH.exists():
            raise FileNotFoundError(f"Metadata file not found: {METADATA_PATH}")

        self.model = joblib.load(MODEL_PATH)

        with open(METADATA_PATH, "r") as f:
            self.metadata = json.load(f)

        self.expected_features = self.metadata["features"]["input_features"]

    def validate_input(self, transaction_data: dict):
        incoming_features = list(transaction_data.keys())

        missing_features = [f for f in self.expected_features if f not in incoming_features]
        extra_features = [f for f in incoming_features if f not in self.expected_features]

        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")

        if extra_features:
            raise ValueError(f"Unexpected features: {extra_features}")

    def predict_proba(self, transaction_data: dict) -> float:
        self.validate_input(transaction_data)

        input_df = pd.DataFrame([transaction_data])
        input_df = input_df[self.expected_features]

        fraud_prob = self.model.predict_proba(input_df)[:, 1][0]
        return float(fraud_prob)

    @property
    def version(self) -> str:
        return self.metadata["version"]