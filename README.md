<div align="center">

# 🧠 MentalHealth-AI-Risk-Detection

### Transformer-based AI platform for detecting **depression and suicide risk** from Reddit posts

<p>

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

AI system that analyzes **Reddit posts** and predicts **depression and suicide risk** using  
**BERT / RoBERTa NLP models + Explainable AI + Real-time API services**

</div>

---

# 📌 Overview

Mental health issues such as **depression** and **suicidal ideation** are frequently expressed on social media.

This project builds a **scalable AI platform** that detects early warning signals from Reddit posts using **state-of-the-art transformer models**.

The system combines:

* 🧠 Transformer NLP Models
* 🔎 Explainable AI
* ⚡ FastAPI inference services
* 📊 Interactive analytics dashboard

⚠️ **Disclaimer**

This project is intended **for research and educational purposes only**.  
It must **not be used as a clinical diagnostic system**.

---

# 🚀 Key Features

✔ Depression detection from text  
✔ Suicide risk prediction  
✔ Transformer NLP models (**BERT / RoBERTa**)  
✔ Ensemble prediction system  
✔ Explainable AI (**SHAP + LIME**)  
✔ FastAPI backend  
✔ Streamlit clinician dashboard  
✔ Automated retraining pipeline  
✔ Model drift monitoring  
✔ Docker & Kubernetes deployment  

---

# 🏗 System Architecture

```
Reddit API
    │
    ▼
Data Ingestion
    │
    ▼
Data Processing Pipeline
    │
    ▼
Transformer NLP Models
(BERT / RoBERTa / Ensemble)
    │
    ▼
Explainable AI
(SHAP / LIME)
    │
    ▼
FastAPI Prediction API
    │
 ┌──┴───────────┐
 ▼              ▼
Dashboard   Alert System
```

---

# 📂 Project Structure

```bash
mental-health-ai-platform/

data_pipeline/
    reddit_scraper.py
    data_validation.py

nlp_models/
    bert_classifier.py
    roberta_classifier.py
    ensemble_model.py

explainability/
    shap_explainer.py
    lime_explainer.py

backend/
    api_server.py

dashboard/
    clinician_dashboard.py

monitoring/
    model_drift.py
    bias_detection.py

retraining/
    automated_training.py

deployment/
    docker/
    kubernetes/

configs/
    model_config.yaml
```

---

# 🧠 Machine Learning Models

| Model | Purpose |
|------|------|
| **BERT** | Baseline depression classifier |
| **RoBERTa** | Advanced contextual understanding |
| **Ensemble Model** | Combines predictions |

---

# 📊 Model Benchmark (Example)

| Model | Accuracy | F1 Score | ROC-AUC |
|------|------|------|------|
| Logistic Regression | 0.74 | 0.71 | 0.76 |
| LSTM | 0.83 | 0.82 | 0.85 |
| **BERT** | **0.90** | **0.88** | **0.92** |
| **RoBERTa** | **0.92** | **0.90** | **0.94** |

---

# 📊 Risk Classification

| Risk Level | Description |
|------|------|
| Low | Normal conversation |
| Moderate | Possible depression |
| High | Severe depression indicators |
| Critical | Possible suicidal ideation |

Example post

```
"I feel like my life has no meaning anymore."
```

Prediction

```
Risk Score: 0.91
Risk Level: Critical
Recommendation: Immediate mental health support
```

---

# 🔎 Explainable AI

The system provides **interpretable predictions**.

### SHAP

Shows **global feature importance** across the dataset.

### LIME

Explains **individual predictions**.

Example risk indicators:

```
hopeless
meaningless
end my life
can't go on
```

---

# 🎬 Demo

Example dashboard interface:

```
User Input → Reddit Post
        ↓
Risk Score → 0.87
Risk Level → High
Recommendation → Professional counseling suggested
```

---

# 🔌 API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
"status": "ok"
}
```

---

### Predict Mental Health Risk

```
POST /predict
```

Request

```json
{
"text": "I feel hopeless and tired of life"
}
```

Response

```json
{
"risk_score": 0.92,
"recommendation": "Immediate crisis hotline recommendation"
}
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/yourusername/MentalHealth-AI-Risk-Detection.git
cd MentalHealth-AI-Risk-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Platform

Collect data

```bash
python data_pipeline/reddit_scraper.py
```

Train model

```bash
python retraining/automated_training.py
```

Start API

```bash
uvicorn backend.api_server:app --reload
```

Launch dashboard

```bash
streamlit run dashboard/clinician_dashboard.py
```

---

# 🐳 Docker Deployment

Build container

```bash
docker build -t mental-health-ai .
```

Run container

```bash
docker run -p 8000:8000 mental-health-ai
```

---

# 📚 Datasets

Recommended datasets

• Reddit Mental Health Dataset  
• CLPsych 2015 Shared Task  
• Depression Reddit Dataset  

Sources

https://huggingface.co/datasets  
https://reddit.com

---

# 🛠 Technology Stack

| Layer | Technology |
|------|------|
Machine Learning | PyTorch |
NLP | HuggingFace Transformers |
Explainability | SHAP, LIME |
API | FastAPI |
Dashboard | Streamlit |
Deployment | Docker, Kubernetes |

---

# ⚠️ Ethical Considerations

Mental health AI must be used responsibly.

• AI should **assist clinicians, not replace them**  
• Predictions require **human interpretation**  
• Systems must **avoid bias**  
• Crisis resources should always be available  

---

# 🤝 Contributing

Contributions are welcome.

Possible improvements:

* Better NLP models
* Additional datasets
* Dashboard enhancements
* Monitoring pipelines

---

# ⭐ Support

If you find this project useful

⭐ Star the repository  
🍴 Fork the project  
📢 Share with the community  

---

# 📜 License

MIT License

---

# 🏷 GitHub Topics

```
mental-health
nlp
machine-learning
transformers
bert
roberta
suicide-prevention
fastapi
streamlit
ai-healthcare
```
