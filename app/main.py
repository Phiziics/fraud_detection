from fastapi import FastAPI, HTTPException

from app.config import APP_NAME, APP_VERSION
from app.schemas import PredictionResponse, TransactionInput
from app.fraud_service import score_transaction

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionInput):
    try:
        return score_transaction(transaction.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")