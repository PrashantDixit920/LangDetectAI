from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    
def test_languages_endpoint():

    response = client.get("/api/v1/languages")

    assert response.status_code == 200

    data = response.json()

    assert "languages" in data

    assert len(data["languages"]) == 10    
    
    
def test_model_info_endpoint():

    response = client.get("/api/v1/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model"] == "Character-Level LSTM"
    assert data["languages"] == 10
    assert data["max_sequence_length"] == 650
    assert data["test_accuracy"] == 0.99 
    
def test_prediction_endpoint():

    response = client.post(
        "/api/v1/predict",
        json={
            "text": "This is a test sentence in English."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "language" in data
    assert "confidence" in data

    assert data["language"] in [
        "Arabic",
        "Chinese",
        "English",
        "French",
        "German",
        "Hindi",
        "Italian",
        "Portuguese",
        "Russian",
        "Spanish"
    ]

    assert 0 <= data["confidence"] <= 1    
    
def test_prediction_empty_text():

    response = client.post(
        "/api/v1/predict",
        json={
            "text": ""
        }
    )

    assert response.status_code == 422
    
def test_prediction_whitespace_text():

    response = client.post(
        "/api/v1/predict",
        json={
            "text": "     "
        }
    )

    assert response.status_code == 422   
    
def test_prediction_text_too_long():

    response = client.post(
        "/api/v1/predict",
        json={
            "text": "a" * 5001
        }
    )

    assert response.status_code == 422     
    
def test_prediction_service_error(monkeypatch):

    def mock_predict_language(text):
        raise Exception("Model failure")

    monkeypatch.setattr(
        "app.api.routes.predict_language",
        mock_predict_language
    )

    response = client.post(
        "/api/v1/predict",
        json={
            "text": "This is a test sentence."
        }
    )

    assert response.status_code == 500

    data = response.json()

    assert data["detail"] == "Prediction service failed."        