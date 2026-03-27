from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION
from app.schemas import TransactionInput, PredictionResponse
from app.fraud_service import score_transaction

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionInput):
    result = score_transaction(transaction.dict())
    return result