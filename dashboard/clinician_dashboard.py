
import streamlit as st
from nlp_models.ensemble_model import EnsembleModel
from recommendation_engine.intervention_generator import recommend

st.title("Mental Health Risk Monitoring Dashboard")

model = EnsembleModel()

text = st.text_area("Enter Reddit Post")

if st.button("Analyze"):
    score = model.predict(text)
    rec = recommend(score)

    st.write("Risk Score:", score)
    st.write("Recommendation:", rec)
