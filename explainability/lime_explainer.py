
from lime.lime_text import LimeTextExplainer

def explain(predict_fn, text):
    explainer = LimeTextExplainer(class_names=["safe","risk"])
    exp = explainer.explain_instance(text, predict_fn)
    return exp.as_list()
