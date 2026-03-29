
import torch
from transformers import BertTokenizer, BertForSequenceClassification

class BertClassifier:

    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        return probs[0][1].item()
