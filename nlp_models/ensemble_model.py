
from nlp_models.bert_classifier import BertClassifier
from nlp_models.roberta_classifier import RobertaClassifier

class EnsembleModel:

    def __init__(self):
        self.bert = BertClassifier()
        self.roberta = RobertaClassifier()

    def predict(self, text):
        p1 = self.bert.predict(text)
        p2 = self.roberta.predict(text)
        return (p1 + p2) / 2
