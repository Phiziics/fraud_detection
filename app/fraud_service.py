from app.config import FRAUD_THRESHOLD
from app.fraud_model import FraudModel

model = FraudModel()


def get_risk_label(probability: float) -> str:
    if probability >= 0.80:
        return "high"
    if probability >= FRAUD_THRESHOLD:
        return "medium"
    return "low"


def score_transaction(transaction_data: dict) -> dict:
    fraud_probability = model.predict_proba(transaction_data)
    is_fraud = fraud_probability >= FRAUD_THRESHOLD
    risk_label = get_risk_label(fraud_probability)

    return {
        "fraud_probability": round(fraud_probability, 6),
        "threshold_used": FRAUD_THRESHOLD,
        "is_fraud": is_fraud,
        "risk_label": risk_label,
    }