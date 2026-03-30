from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

MODEL_VERSION = "1.0"
MODEL_PATH = ARTIFACTS_DIR / f"fraud_model_v{MODEL_VERSION}.joblib"
METADATA_PATH = ARTIFACTS_DIR / f"fraud_model_v{MODEL_VERSION}_metadata.json"

FRAUD_THRESHOLD = 0.30
APP_NAME = "Fraud Detection API"
APP_VERSION = "1.0.0"