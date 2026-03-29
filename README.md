<div align="center">

# 🧠 MentalHealth-AI-Risk-Detection

### AI platform for detecting **depression and suicide risk** from Reddit posts using **Transformer NLP models**

<p>

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red.svg)
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

Mental health conditions such as **depression and suicidal ideation** are often expressed in online communities.

This project builds a **scalable AI platform** capable of detecting early warning signals from social media text.

The platform integrates:

- 🧠 **Transformer NLP Models**
- 🔎 **Explainable AI**
- ⚡ **FastAPI prediction services**
- 📊 **Interactive clinician dashboard**

> ⚠️ **Disclaimer**  
> This system is for **research and educational purposes only** and **must not be used as a clinical diagnostic tool.**

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

```text
                Reddit API
                     │
                     ▼
              Data Ingestion
                     │
                     ▼
              Data Processing
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
                FastAPI API
                     │
           ┌─────────┴─────────┐


 📂 Project Structure
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
🧠 Machine Learning Models

The system uses Transformer-based NLP models.

Model	Purpose
BERT	Baseline depression classifier
RoBERTa	Advanced contextual understanding
Ensemble Model	Combines predictions
📊 Risk Classification
Risk Level	Description
Low	Normal conversation
Moderate	Possible depression
High	Severe depression indicators
Critical	Possible suicidal ideation

Example post:

"I feel like my life has no meaning anymore."

Prediction:

Risk Score: 0.91
Risk Level: Critical
Recommendation: Immediate mental health support
🔎 Explainable AI

To ensure transparency, the system includes model explanations.

SHAP

Shows global feature importance.

LIME

Explains individual predictions.

Example indicators:

hopeless
meaningless
end my life
can't go on
🔌 API Endpoints
Health Check
GET /health

Response

{
  "status": "ok"
}
Predict Mental Health Risk
POST /predict

Request

{
"text": "I feel hopeless and tired of life"
}

Response

{
"risk_score":0.92,
"recommendation":"Immediate crisis hotline recommendation"
}
⚙️ Installation

Clone repository

git clone https://github.com/yourusername/MentalHealth-AI-Risk-Detection.git
cd MentalHealth-AI-Risk-Detection

Install dependencies

pip install -r requirements.txt
▶️ Running the Platform
Collect Data
python data_pipeline/reddit_scraper.py
Train Model
python retraining/automated_training.py
Start API
uvicorn backend.api_server:app --reload
Launch Dashboard
streamlit run dashboard/clinician_dashboard.py
🐳 Docker Deployment

Build container

docker build -t mental-health-ai .

Run container

docker run -p 8000:8000 mental-health-ai
📚 Datasets

Recommended datasets:

• Reddit Mental Health Dataset
• CLPsych 2015 Shared Task
• Depression Reddit Dataset

Sources:

https://huggingface.co/datasets
https://reddit.com
🛠 Technology Stack
Layer	Technology
Machine Learning	PyTorch
NLP	HuggingFace Transformers
Explainability	SHAP, LIME
API	FastAPI
Dashboard	Streamlit
Deployment	Docker, Kubernetes
⚠️ Ethical Considerations

Mental health AI must be used responsibly.

AI should assist clinicians, not replace them
Predictions require human interpretation
Systems must avoid bias
Crisis resources should always be available
🤝 Contributing

Contributions are welcome.

Possible improvements:

Better NLP models
Additional datasets
Dashboard enhancements
Monitoring pipelines
⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with the community

📜 License

MIT License
           ▼                   ▼
     Streamlit Dashboard   Alert System
