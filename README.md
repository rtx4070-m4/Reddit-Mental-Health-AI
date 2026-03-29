
# Mental Health AI Platform (1000x Version)

Enterprise-style platform for detecting depression and suicide risk from Reddit posts.

Features
- Reddit data ingestion
- Transformer NLP models (BERT/RoBERTa)
- Explainable AI (SHAP + LIME)
- FastAPI backend
- Streamlit clinician dashboard
- Model monitoring and drift detection
- Automated retraining pipeline
- Docker + Kubernetes deployment

Run locally:

pip install -r requirements.txt
python data_pipeline/reddit_scraper.py
python retraining/automated_training.py
uvicorn backend.api_server:app --reload
streamlit run dashboard/clinician_dashboard.py
