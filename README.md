# LangDetectAI

**LangDetectAI** is an AI-powered language identification system that uses a **character-level LSTM neural network** to identify the language of input text. The project provides a polished web interface, REST API, input validation, model information endpoints, automated tests, and interactive API documentation.

The system currently supports **10 languages** and achieves approximately **99% test accuracy** on an unseen test set.

---

## 🚀 Features

* 🌍 Language identification across 10 languages
* 🧠 Character-level LSTM neural network
* ⚡ FastAPI REST API
* 🖥️ Responsive web interface
* 🌙 Light/Dark mode
* 📊 Confidence score for predictions
* ✅ Request validation using Pydantic
* 🔍 Health-check endpoint
* 📋 Supported-language endpoint
* 🤖 Model-information endpoint
* 📚 Interactive API documentation
* 🧪 Automated API and prediction tests
* 🧹 Emoji-aware preprocessing
* 📦 Saved model and preprocessing artifacts
* 🏗️ Modular backend architecture

---

## 🌍 Supported Languages

| Language   |
| ---------- |
| Arabic     |
| Chinese    |
| English    |
| French     |
| German     |
| Hindi      |
| Italian    |
| Portuguese |
| Russian    |
| Spanish    |

---

## 🧠 Machine Learning Model

LangDetectAI uses a **character-level LSTM architecture**.

Instead of treating an input sentence as a sequence of words, the model processes it as a sequence of characters.

For example:

```text
"Hello world"
      ↓
H → e → l → l → o →   → w → o → r → l → d
      ↓
Character IDs
      ↓
Embedding
      ↓
LSTM
      ↓
Dense Layer
      ↓
Softmax
      ↓
English
```

Character-level processing is particularly useful for language identification because languages often have distinctive:

* Character sets
* Scripts
* Character combinations
* Accented characters
* Orthographic patterns

It also avoids depending on a fixed vocabulary of complete words.

---

## 🏗️ Model Architecture

```text
Input Text
    │
    ▼
Character Tokenization
    │
    ▼
Integer Sequences
    │
    ▼
Padding / Truncation
    │
    ▼
Embedding Layer
    │
    ▼
LSTM Layer
    │
    ▼
Dense Layer
    │
    ▼
Softmax Output
    │
    ▼
Predicted Language
```

### Model configuration

| Component               | Configuration |
| ----------------------- | ------------: |
| Vocabulary size         |         2,753 |
| Maximum sequence length |           650 |
| Embedding dimension     |            64 |
| LSTM units              |           128 |
| Dense units             |            64 |
| Output classes          |            10 |
| Total parameters        |       283,914 |

### Architecture

```text
Embedding
    ↓
650 × 64

LSTM
    ↓
128 units

Dense
    ↓
64 units
ReLU

Output
    ↓
10 units
Softmax
```

---

## 📊 Model Performance

The model was evaluated on an unseen test set containing **6,914 samples**.

### Overall performance

**Test Accuracy: ~99%**

The classification report showed strong performance across all 10 languages.

| Language   | Precision | Recall | F1-Score |
| ---------- | --------: | -----: | -------: |
| Arabic     |      1.00 |   1.00 |     1.00 |
| Chinese    |      1.00 |   1.00 |     1.00 |
| English    |      0.99 |   0.99 |     0.99 |
| French     |      0.98 |   0.99 |     0.99 |
| German     |      1.00 |   0.99 |     0.99 |
| Hindi      |      1.00 |   1.00 |     1.00 |
| Italian    |      0.98 |   0.99 |     0.98 |
| Portuguese |      0.96 |   0.97 |     0.97 |
| Russian    |      1.00 |   1.00 |     1.00 |
| Spanish    |      0.99 |   0.98 |     0.99 |

> Performance is based on the project's held-out test set and should not be interpreted as universal real-world accuracy.

---

## 🔄 Prediction Pipeline

When a user submits text, the following pipeline is executed:

```text
User Input
    │
    ▼
FastAPI Request Validation
    │
    ▼
Emoji Removal
    │
    ▼
Character Tokenization
    │
    ▼
Integer Sequence
    │
    ▼
Padding / Truncation
    │
    ▼
LSTM Model
    │
    ▼
Class Prediction
    │
    ▼
Label Encoder
    │
    ▼
Language + Confidence
    │
    ▼
JSON Response
```

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn

### Backend

* FastAPI
* Uvicorn
* Pydantic
* Jinja2

### Frontend

* HTML5
* CSS3
* JavaScript

### Testing

* Pytest
* HTTPX

### Development

* Git
* GitHub
* VS Code
* Google Colab

---

## 📁 Project Structure

```text
LangDetectAI/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── model/
│   │   ├── language_detection_model.keras
│   │   ├── language_detection_tokenizer.pkl
│   │   ├── language_detection_label_encoder.pkl
│   │   └── config.pkl
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── model_manager.py
│   │   ├── preprocessing.py
│   │   └── predictor.py
│   │
│   ├── static/
│   │   ├── assets/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── predict.html
│   │   ├── about.html
│   │   └── documentation.html
│   │
│   └── main.py
│
├── data/
│   └── dataset files
│
├── notebooks/
│   └── language_detection.ipynb
│
├── tests/
│   ├── test_api.py
│   └── test_prediction.py
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

---

## 🔌 REST API

The application exposes versioned API endpoints under:

```text
/api/v1
```

### Available endpoints

| Method | Endpoint             | Purpose                    |
| ------ | -------------------- | -------------------------- |
| GET    | `/api/v1/health`     | Check API and model status |
| GET    | `/api/v1/languages`  | Get supported languages    |
| GET    | `/api/v1/model-info` | Get model information      |
| POST   | `/api/v1/predict`    | Predict the language       |

---

## 🔮 Prediction API

### Endpoint

```http
POST /api/v1/predict
```

### Request

```json
{
    "text": "This is a language detection example."
}
```

### Response

```json
{
    "language": "English",
    "confidence": 0.9629
}
```

The `confidence` value represents the model's highest predicted class probability.

---

## 🩺 Health Check

### Endpoint

```http
GET /api/v1/health
```

### Example response

```json
{
    "status": "healthy",
    "model_loaded": true
}
```

---

## 🌍 Get Supported Languages

### Endpoint

```http
GET /api/v1/languages
```

### Example response

```json
{
    "languages": [
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
    ],
    "count": 10
}
```

---

## 🤖 Model Information

### Endpoint

```http
GET /api/v1/model-info
```

### Example response

```json
{
    "model": "Character-Level LSTM",
    "languages": 10,
    "max_sequence_length": 650,
    "test_accuracy": 0.99
}
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, open:

```text
/docs
```

This provides an interactive Swagger UI where API endpoints can be tested directly from the browser.

FastAPI also provides an alternative ReDoc interface:

```text
/redoc
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project

```bash
cd LangDetectAI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

The API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

LangDetectAI includes automated tests covering the API, validation, preprocessing, and prediction functionality.

Run all tests from the project root:

```bash
python -m pytest
```

The current test suite contains **16 tests**, covering:

* Health endpoint
* Supported languages endpoint
* Model information endpoint
* Prediction endpoint
* Empty input validation
* Whitespace validation
* Maximum input length validation
* Prediction response structure
* English prediction
* French prediction
* Hindi prediction
* Emoji preprocessing
* Preprocessing output shape
* Short text prediction
* Emoji prediction
* Prediction service failure handling

---

## 🔐 Input Validation

The API validates incoming prediction requests using Pydantic.

Current validation rules include:

* Text must not be empty.
* Text cannot contain only whitespace.
* Maximum input length is 5,000 characters.

Invalid requests return an appropriate HTTP validation response instead of being passed directly to the model.

---

## 🧩 Model Artifacts

The application requires four saved artifacts:

```text
language_detection_model.keras
language_detection_tokenizer.pkl
language_detection_label_encoder.pkl
config.pkl
```

### Model

Contains the trained character-level LSTM neural network.

### Tokenizer

Converts input characters into the integer IDs expected by the model.

### Label Encoder

Converts the model's numerical output class back into a human-readable language name.

### Configuration

Stores important model configuration such as:

```json
{
    "vocab_size": 2753,
    "max_len": 650
}
```

Keeping these artifacts together ensures that inference uses the same preprocessing and label mapping as training.

---

## 🧠 Why Character-Level LSTM?

Language identification is a good use case for character-level modeling.

Consider:

```text
English:
"the", "tion", "ing"

French:
"que", "tion", "ment"

German:
"sch", "ung", "lich"
```

The model can learn patterns at the character level without requiring complete words to exist in its vocabulary.

Character-level processing can also help with:

* Unseen words
* Misspellings
* Different word forms
* Multilingual text
* Script-based identification

---

## ⚠️ Limitations

Although the model performs strongly on the evaluation dataset, it has several limitations.

### 1. Limited language coverage

The current model supports only 10 languages.

### 2. Short text

Very short inputs may contain insufficient linguistic information.

For example:

```text
"hi"
```

can be difficult to classify reliably.

### 3. Similar languages

Languages with similar vocabulary and writing patterns can be more difficult to distinguish.

For example:

```text
Italian ↔ Portuguese
French ↔ Portuguese
Spanish ↔ Portuguese
```

### 4. Code-switching

Mixed-language sentences may produce less reliable predictions.

Example:

```text
"Main आज office जा रहा हूँ."
```

### 5. Domain differences

The model's performance on new domains may differ from its performance on the evaluation dataset.

### 6. Confidence is not certainty

A high model confidence score does not guarantee that the prediction is correct.

---

## 🔮 Future Improvements

Potential future improvements include:

* Add more languages
* Add confusion-matrix visualization
* Improve detection of closely related languages
* Experiment with GRU and Bidirectional LSTM
* Compare character-level and word-level models
* Experiment with CNN-LSTM architectures
* Add transformer-based language identification
* Add probability distribution for all languages
* Add batch prediction
* Add multilingual mixed-text detection
* Add rate limiting
* Add structured application logging
* Add Docker deployment
* Add CI/CD using GitHub Actions
* Deploy the application to a cloud platform
* Add production monitoring

---

## 🔄 Future Architecture

A future production version could evolve toward:

```text
                    ┌─────────────────┐
                    │     Client      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    │      API        │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Validation    │
                    │   & Preprocess  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Language Model  │
                    │ LSTM / Transformer│
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    Prediction   │
                    │  + Confidence   │
                    └─────────────────┘
```

---

## 🎯 Project Goals

LangDetectAI was built to demonstrate an end-to-end machine learning application rather than only a model-training notebook.

The project combines:

```text
Machine Learning
       +
Deep Learning
       +
Natural Language Processing
       +
FastAPI
       +
Frontend Development
       +
REST API Design
       +
Input Validation
       +
Automated Testing
       +
Software Architecture
```

---

## 📌 Key Learning Outcomes

This project demonstrates practical experience with:

* Text preprocessing
* Character-level tokenization
* Sequence padding
* Label encoding
* Embedding layers
* LSTM networks
* Multiclass classification
* Model evaluation
* Model serialization
* FastAPI
* REST APIs
* Pydantic validation
* Jinja2 templates
* HTML/CSS/JavaScript
* API testing
* Project structuring
* Separation of concerns
* Git/GitHub workflow

---

## 👨‍💻 Author

**Prashant Dixit**

B.Tech Computer Science & Engineering — Artificial Intelligence & Machine Learning

---

## 📄 License

This project is intended for educational and portfolio purposes.

If you choose to distribute or modify the project, add an appropriate open-source license such as MIT License according to your intended usage.
