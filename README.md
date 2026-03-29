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
           ▼                   ▼
     Streamlit Dashboard   Alert System
