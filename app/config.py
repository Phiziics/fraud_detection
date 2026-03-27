from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "fraud_model.joblib"

FRAUD_THRESHOLD = 0.30
APP_NAME = "Fraud Detection API"
APP_VERSION = "1.0.0"