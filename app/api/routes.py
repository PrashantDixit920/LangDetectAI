from fastapi import APIRouter, HTTPException

from app.services.model_manager import (
    model,
    label_encoder,
    MAX_LEN
)

from app.api.schemas import (
    PredictionRequest,
    PredictionResponse
)

from app.services.predictor import predict_language


router = APIRouter(
    prefix="/api/v1",
    tags=["Prediction"]
)


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    try:

        result = predict_language(request.text)

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail="Prediction service failed."
        ) from error

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@router.get("/languages")
def get_languages():
    languages = label_encoder.classes_.tolist()

    return {
        "languages": languages,
        "count": len(languages)
    }


@router.get("/model-info")
def model_info():
    return {
        "model": "Character-Level LSTM",
        "languages": len(label_encoder.classes_),
        "max_sequence_length": MAX_LEN,
        "test_accuracy": 0.99
    }    