
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

class RobertaClassifier:

    def __init__(self):
        self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
        self.model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=2)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        return probs[0][1].item()
