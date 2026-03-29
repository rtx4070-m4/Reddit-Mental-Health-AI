🧠 MentalHealth-AI-Risk-Detection












AI platform for detecting depression and suicide risk from Reddit posts using Transformer-based NLP models (BERT / RoBERTa) with Explainable AI, FastAPI microservices, and an interactive clinician dashboard.

📌 Overview

Mental health conditions such as depression and suicidal ideation are often expressed on social media platforms.

This project builds a scalable AI system capable of detecting early warning signals from textual content.

The platform integrates:

Transformer NLP models
Explainable AI
Microservice APIs
Interactive analytics dashboards

The goal is to support mental health research and early risk detection systems.

⚠️ Disclaimer

This system is for research and educational purposes only and must not be used as a clinical diagnostic tool.

🚀 Key Features

✔ Depression detection from Reddit posts
✔ Suicide risk prediction
✔ Transformer NLP models (BERT / RoBERTa)
✔ Ensemble model prediction system
✔ Explainable AI with SHAP and LIME
✔ FastAPI prediction API
✔ Streamlit clinician dashboard
✔ Automated retraining pipeline
✔ Model drift monitoring
✔ Docker and Kubernetes deployment support

🏗 System Architecture
                 Reddit API
                      │
                      ▼
              Data Ingestion Layer
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
                 FastAPI Service
                      │
           ┌──────────┴───────────┐
           ▼                      ▼
   Streamlit Dashboard      Alert System
📂 Project Structure
mental-health-ai-platform/

data_pipeline/
    reddit_scraper.py
    data_validation.py
    streaming_consumer.py

nlp_models/
    bert_classifier.py
    roberta_classifier.py
    ensemble_model.py

explainability/
    shap_explainer.py
    lime_explainer.py

recommendation_engine/
    intervention_generator.py

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

tests/
🧠 Machine Learning Models

The system uses state-of-the-art transformer models.

Model	Purpose
BERT	Baseline depression classifier
RoBERTa	Improved contextual understanding
Ensemble Model	Combines model predictions
📊 Mental Health Risk Classification
Risk Level	Meaning
Low	Normal conversation
Moderate	Possible depression indicators
High	Severe depressive language
Critical	Possible suicidal ideation

Example post:

"I feel like my life has no meaning and I can't go on anymore."

Prediction:

Risk Score: 0.91
Risk Level: Critical
Recommendation: Immediate support resources
🔎 Explainable AI

The platform includes transparent AI explanations.

SHAP

Global feature importance across predictions.

LIME

Local explanations for individual posts.

Example indicators:

hopeless
meaningless
end my life
can't go on
📊 Clinician Dashboard

The Streamlit interface allows users to:

Analyze Reddit posts
View risk scores
See recommendations
Explore explanation graphs
Monitor trends

Example output:

Risk Score: 0.87
Risk Level: High
Recommendation: Encourage professional counseling
🔌 API Endpoints
Health Check
GET /health

Response

{"status":"ok"}
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
1️⃣ Collect Reddit Data
python data_pipeline/reddit_scraper.py
2️⃣ Train Model
python retraining/automated_training.py
3️⃣ Start API
uvicorn backend.api_server:app --reload
4️⃣ Launch Dashboard
streamlit run dashboard/clinician_dashboard.py
🐳 Docker Deployment

Build container

docker build -t mental-health-ai .

Run container

docker run -p 8000:8000 mental-health-ai
📚 Datasets

Potential datasets for training:

Reddit Mental Health Dataset
CLPsych 2015 Shared Task
Depression Reddit Dataset

Example sources:

https://www.reddit.com
https://huggingface.co/datasets
📈 Future Work

Possible research extensions:

Real-time Reddit streaming pipeline
LLM-based mental health chatbot
GPU distributed training
Bias and fairness evaluation
Clinical validation studies
Mobile application interface
⚠️ Ethical Considerations

Mental health AI systems must be developed responsibly.

Guidelines:

AI should assist, not replace clinicians
Predictions must be interpreted by experts
Systems should avoid demographic bias
Users must have access to crisis resources
🛠 Technology Stack
Layer	Technology
Machine Learning	PyTorch
NLP	HuggingFace Transformers
Explainability	SHAP, LIME
API	FastAPI
Dashboard	Streamlit
Data	Reddit API
Deployment	Docker, Kubernetes
🤝 Contributing

Contributions are welcome.

Possible contributions:

Improving NLP models
Adding datasets
Enhancing dashboards
Implementing monitoring systems
📜 License

MIT License

⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with the community
