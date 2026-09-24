# LangDetectAI 🌐

An AI-powered multilingual language identification system built with **TensorFlow, LSTM, FastAPI, and JavaScript**, capable of identifying the language of user-provided text across 10 supported languages.

---

## 📌 Overview

**LangDetectAI** solves the problem of automatically identifying the language of a given text.

Language identification is an important NLP task used in applications such as:

* Multilingual chatbots
* Translation systems
* Content moderation
* Search engines
* Customer-support systems
* Document processing
* Language-aware recommendation systems

LangDetectAI uses a **character-level LSTM neural network** to analyze text patterns and classify the input into one of 10 supported languages.

The trained model is exposed through a **FastAPI REST API** and integrated with a responsive HTML/CSS/JavaScript frontend. The complete application is also **Dockerized** for reproducible deployment.

---

## ✨ Features

* 🌍 Supports **10 languages**
* 🧠 Character-level **LSTM-based NLP model**
* 🎯 Approximately **99% test accuracy**
* ⚡ FastAPI REST API
* 🛡️ Pydantic request validation
* 🔄 Real-time language prediction
* 📊 Prediction confidence score
* 🖥️ Responsive web interface
* 🌙 Light/Dark theme
* 📚 Interactive Swagger API documentation
* ❤️ Health-check endpoint
* 🧪 Automated API and prediction tests
* 🐳 Dockerized deployment
* 📦 Saved model and preprocessing artifacts
* 🏗️ Modular production-style project structure

---

## 🌎 Supported Languages

LangDetectAI currently supports:

1. Arabic
2. Chinese
3. English
4. French
5. German
6. Hindi
7. Italian
8. Portuguese
9. Russian
10. Spanish

---

## 🧠 Machine Learning Model

The project uses a **character-level LSTM neural network**.

### Model Architecture

```text
Input Text
    ↓
Character Tokenization
    ↓
Sequence Padding
    ↓
Embedding Layer
    ↓
LSTM (128 units)
    ↓
Dense (64 units, ReLU)
    ↓
Dense (10 units, Softmax)
    ↓
Predicted Language
```

### Model Configuration

| Parameter               |                Value |
| ----------------------- | -------------------: |
| Input type              | Character-level text |
| Vocabulary size         |                2,753 |
| Maximum sequence length |                  650 |
| Embedding dimension     |                   64 |
| LSTM units              |                  128 |
| Dense units             |                   64 |
| Output classes          |                   10 |
| Total parameters        |              283,914 |
| Framework               |   TensorFlow / Keras |

---

## 📊 Model Performance

The model achieves approximately **99% accuracy on the test dataset**.

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

> Performance values are based on the project's held-out test dataset and should not be interpreted as real-world performance across all possible text domains.

---

## 📚 Dataset

The project uses the **Language Identification Dataset** from Hugging Face:

`papluca/language-identification`

The dataset was processed specifically for this project.

### Data Processing

The preprocessing pipeline included:

1. Selecting the required 10 languages
2. Converting labels to full language names
3. Removing duplicate text entries
4. Removing emojis
5. Fitting the tokenizer only on training data
6. Converting text into character sequences
7. Padding/truncating sequences to a maximum length of 650
8. Encoding target labels using `LabelEncoder`

A total of **431 duplicate text entries** were removed during preprocessing.

### Processed Dataset

```text
Training samples: 27,655
Testing samples:   6,914
```

---

## 🔄 Prediction Pipeline

The complete prediction pipeline is:

```text
User Input
    ↓
FastAPI Request
    ↓
Pydantic Validation
    ↓
Emoji Removal
    ↓
Character Tokenization
    ↓
Sequence Padding
    ↓
LSTM Model
    ↓
Softmax Probabilities
    ↓
Argmax
    ↓
Label Encoder
    ↓
Language + Confidence
    ↓
JSON Response
    ↓
Frontend
```

---

## 🏗️ Project Architecture

```text
LangDetectAI/
│
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
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
│   │   └── language_detection_config.pkl
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
│   │   │   ├── about.css
│   │   │   ├── documentation.css
│   │   │   ├── home.css
│   │   │   ├── predict.css
│   │   │   └── style.css
│   │   │
│   │   └── js/
│   │       ├── documentation.js
│   │       ├── main.js
│   │       └── predict.js
│   │
│   ├── templates/
│   │   ├── about.html
│   │   ├── documentation.html
│   │   ├── index.html
│   │   └── predict.html
│   │
│   └── main.py
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── notebooks/
│   └── language_detection.ipynb
│
└── tests/
    ├── __init__.py
    ├── test_api.py
    └── test_prediction.py
```

---

## ⚙️ Tech Stack

### Machine Learning / NLP

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn

### Backend

* FastAPI
* Pydantic
* Uvicorn
* Jinja2

### Frontend

* HTML5
* CSS3
* JavaScript

### Testing

* Pytest
* HTTPX

### Deployment / DevOps

* Docker
* Docker Desktop
* WSL 2
* Git
* GitHub

---

## 🚀 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/PrashantDixit920/LangDetectAI.git
```

Navigate into the project:

```bash
cd LangDetectAI
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://localhost:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## 🔌 REST API

The API uses the following base path:

```text
/api/v1
```

### Predict Language

**POST**

```text
/api/v1/predict
```

Request:

```json
{
    "text": "This is a language detection test."
}
```

Example response:

```json
{
    "language": "English",
    "confidence": 0.99
}
```

---

### Health Check

**GET**

```text
/api/v1/health
```

Example:

```json
{
    "status": "healthy",
    "model_loaded": true
}
```

---

### Supported Languages

**GET**

```text
/api/v1/languages
```

Returns the supported language classes and their count.

---

### Model Information

**GET**

```text
/api/v1/model-info
```

Returns information such as:

* Model name
* Number of supported languages
* Maximum sequence length
* Test accuracy

---

## 🛡️ Input Validation

The API uses **Pydantic** to validate incoming requests.

The prediction endpoint:

* Requires text input
* Rejects empty strings
* Rejects whitespace-only input
* Limits input length to **5,000 characters**
* Returns appropriate validation errors

Example invalid request:

```json
{
    "text": ""
}
```

---

## 🧪 Testing

The project includes automated tests covering:

* Health endpoint
* Language endpoint
* Model information endpoint
* English prediction
* French prediction
* Hindi prediction
* Empty input validation
* Whitespace validation
* Maximum input length validation
* Response structure
* Emoji preprocessing
* Short text prediction
* Model output shape
* Prediction service failure handling

Run all tests using:

```bash
pytest
```

Current test suite:

```text
16 tests
```

---

# 🐳 Docker Deployment

LangDetectAI can be completely containerized using Docker.

The Docker image packages:

* Python runtime
* FastAPI
* TensorFlow
* Required dependencies
* Application source code
* LSTM model
* Tokenizer
* Label encoder
* Configuration files
* Frontend

This makes the application reproducible without depending on the local Python environment.

---

## Docker Prerequisites

Install:

* Docker Desktop
* WSL 2 on Windows

Verify Docker:

```bash
docker --version
```

Verify WSL:

```powershell
wsl -l -v
```

The Ubuntu distribution should use:

```text
VERSION  2
```

---

## Build Docker Image

From the project root:

```bash
docker build -t langdetectai .
```

This creates a Docker image named:

```text
langdetectai
```

Verify the image:

```bash
docker images
```

---

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name langdetectai-container langdetectai
```

The application will now be available at:

```text
http://localhost:8000
```

---

## Docker API Documentation

Swagger:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## Docker Container Commands

### Check running containers

```bash
docker ps
```

### View logs

```bash
docker logs langdetectai-container
```

### Stop the container

```bash
docker stop langdetectai-container
```

### Start the container again

```bash
docker start langdetectai-container
```

### Remove the container

```bash
docker rm -f langdetectai-container
```

---

## 🐳 Docker Architecture

```text
Dockerfile
     ↓
docker build
     ↓
Docker Image
     ↓
docker run
     ↓
Docker Container
     │
     ├── FastAPI
     ├── TensorFlow
     ├── LSTM Model
     ├── Model Artifacts
     └── Frontend
     │
     ↓
localhost:8000
```

---

## 📦 Model Artifacts

The trained model and required preprocessing artifacts are stored in:

```text
app/model/
```

### Files

```text
language_detection_model.keras
```

Trained TensorFlow/Keras LSTM model.

```text
language_detection_tokenizer.pkl
```

Character-level tokenizer used during training and inference.

```text
language_detection_label_encoder.pkl
```

Label encoder used to convert model class IDs into language names.

```text
language_detection_config.pkl
```

Stores inference configuration such as:

```text
vocab_size = 2753
max_len = 650
```

Keeping these artifacts together ensures that inference uses the same preprocessing configuration as training.

---

## 🧩 Why Character-Level Modeling?

A character-level approach is useful for language identification because different languages have distinctive:

* Character sets
* Character combinations
* Word structures
* Scripts
* Character sequences
* Orthographic patterns

It can also handle text without requiring a traditional word-level vocabulary.

For example, the model can learn patterns associated with scripts such as:

```text
Latin
Devanagari
Arabic
Cyrillic
Chinese characters
```

---

## 🔐 Environment Variables

The project currently does not require external API keys or sensitive environment variables.

A `.env` file is therefore not required for normal operation.

The `.env` file is included in `.gitignore` to prevent accidental exposure of future secrets or configuration values.

---

## ⚠️ Limitations

Although the model achieves approximately 99% accuracy on the project's test set, real-world performance can vary.

Potential limitations include:

* Very short text
* Mixed-language sentences
* Code-switching
* Names and proper nouns
* Transliteration
* Spelling mistakes
* Domain-specific terminology
* Languages outside the supported 10 classes
* Text containing insufficient linguistic information

The model is designed for **language classification**, not translation.

---

## 🔮 Future Improvements

Possible future improvements include:

* Add more languages
* Improve handling of mixed-language text
* Add language probability distribution
* Add batch prediction
* Add file/document input
* Add model monitoring
* Add CI/CD pipeline
* Deploy using a cloud platform
* Add Docker Compose
* Add API authentication
* Add rate limiting
* Add model versioning
* Add automated model retraining pipeline
* Explore Transformer-based language identification
* Add multilingual dataset expansion

---

## 🎯 Project Goals

The project was developed to demonstrate an end-to-end machine learning application rather than only a trained model.

It combines:

```text
Data Collection
      ↓
Data Cleaning
      ↓
NLP Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Serialization
      ↓
FastAPI Backend
      ↓
Frontend Integration
      ↓
Automated Testing
      ↓
Dockerization
      ↓
GitHub
```

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

### Machine Learning / Deep Learning

* NLP preprocessing
* Character-level tokenization
* Sequence padding
* Embeddings
* LSTM networks
* Multiclass classification
* Softmax prediction
* Model evaluation
* Model serialization

### Backend Development

* FastAPI
* REST APIs
* Pydantic schemas
* Request validation
* Service-layer architecture
* API error handling
* Swagger documentation

### Software Engineering

* Modular project structure
* Separation of concerns
* Automated testing
* Configuration management
* Git/GitHub
* Environment management

### Deployment

* Docker images
* Docker containers
* Dockerfile
* `.dockerignore`
* WSL 2
* Containerized FastAPI deployment

---

## 👨‍💻 Author

**Prashant Dixit**

B.Tech — Computer Science & Engineering (AIML)

GitHub:
https://github.com/PrashantDixit920

LinkedIn:
https://linkedin.com/in/contactprashant-dixit

---

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.
