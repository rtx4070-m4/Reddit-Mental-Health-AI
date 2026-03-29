
from fastapi import FastAPI
from nlp_models.ensemble_model import EnsembleModel
from recommendation_engine.intervention_generator import recommend

app = FastAPI()
model = EnsembleModel()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    score = model.predict(text)
    recommendation = recommend(score)
    return {"risk_score": score, "recommendation": recommendation}
