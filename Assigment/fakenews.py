from lib2to3.pgen2.tokenize import tokenize
from pyexpat import model
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification


model_path = "fake-news-wozz"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
max_length = 512

def get_prediction(text, convert_to_label=False):
# prepare our text into tokenized sequence
    inputs = tokenizer(text, padding=True, truncation=True, max_length=max_length, return_tensors="pt")
    # perform inference to our model
    outputs = model(**inputs)
    # get output probabilities by doing softmax
    probs = outputs[0].softmax(1)
    # executing argmax function to get the candidate label
    d = {
        0: "Reliable",
        1: "Fake"
    }
    if convert_to_label:
        return d[int(probs.argmax())]
    else:
        return int(probs.argmax())


# real_news ="""Tim Tebow Will Attempt Another Comeback, This Time in Baseball -The New York Times",Daniel Victor,"If at first you don't succeed, try a different sport. Tim Tebow, who was a
# Heisman quarterback at the University of Florida but wasunable to hold an N. F. L. job, is pursuing a career in Major League Baseball. <SNIPPED>"""

# print(get_prediction(real_news, convert_to_label=True))
