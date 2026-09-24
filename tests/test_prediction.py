from app.services.predictor import predict_language
from app.services.preprocessing import preprocess_text
from app.services.model_manager import tokenizer, MAX_LEN

def test_predict_language():

    result = predict_language(
        "This is a simple English sentence."
    )

    assert "language" in result
    assert "confidence" in result

    assert result["language"] in [
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

    assert 0 <= result["confidence"] <= 1
    
def test_predict_english():

    result = predict_language(
        "This is a simple sentence written in English."
    )

    assert result["language"] == "English"    
    
def test_predict_french():

    result = predict_language(
        "Bonjour, comment allez-vous aujourd'hui ?"
    )

    assert result["language"] == "French"


def test_predict_hindi():

    result = predict_language(
        "यह एक हिंदी भाषा में लिखा हुआ वाक्य है।"
    )

    assert result["language"] == "Hindi"    
    
def test_preprocess_removes_emoji():

    text = "Hello 😊 this is English."

    result = preprocess_text(
        text,
        tokenizer,
        MAX_LEN
    )

    assert result.shape == (1, MAX_LEN)   
    
def test_preprocess_output_shape():

    text = "This is a test sentence."

    result = preprocess_text(
        text,
        tokenizer,
        MAX_LEN
    )

    assert result.shape == (1, 650)    
    
def test_predict_short_text():

    result = predict_language("Hello")

    assert "language" in result
    assert "confidence" in result

    assert result["language"] in [
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
    
def test_predict_text_with_emoji():

    result = predict_language(
        "Hello, how are you? 😊"
    )

    assert result["language"] == "English"         