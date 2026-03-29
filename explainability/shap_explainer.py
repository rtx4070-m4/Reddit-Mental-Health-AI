
import shap

def explain(model, tokenizer, text):
    explainer = shap.Explainer(model, tokenizer)
    shap_values = explainer([text])
    return shap_values
