import numpy as np

from app.services.preprocessing import preprocess_text
from app.services.model_manager import (
    model,
    tokenizer,
    label_encoder,
    MAX_LEN
)


def predict_language(text):

    # Preprocess text
    input_data = preprocess_text(
        text,
        tokenizer,
        MAX_LEN
    )

    # Get prediction
    prediction = model.predict(
        input_data,
        verbose=0
    )

    # Get predicted class
    predicted_language = np.argmax(
        prediction,
        axis=1
    )[0]

    # Convert class number to language
    language = label_encoder.inverse_transform(
        [predicted_language]
    )[0]

    # Get confidence
    confidence = float(
        np.max(prediction)
    )

    return {
        "language": language,
        "confidence": confidence
    }