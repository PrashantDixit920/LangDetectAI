import pickle
from pathlib import Path

from tensorflow.keras.models import load_model


# Get the app directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model directory
MODEL_DIR = BASE_DIR / "model"


# Load trained model
model = load_model(
    MODEL_DIR / "language_detection_model.keras"
)


# Load tokenizer
with open(
    MODEL_DIR / "language_detection_tokenizer.pkl",
    "rb"
) as file:
    tokenizer = pickle.load(file)


# Load label encoder
with open(
    MODEL_DIR / "language_detection_label_encoder.pkl",
    "rb"
) as file:
    label_encoder = pickle.load(file)


# Load configuration
with open(
    MODEL_DIR / "language_detection_config.pkl",
    "rb"
) as file:
    config = pickle.load(file)


# Extract configuration values
MAX_LEN = config["max_len"]
VOCAB_SIZE = config["vocab_size"]