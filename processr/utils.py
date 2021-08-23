import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "divided", 1: "focused"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "subject": d.subject,
            "solutions": d.solutions,
            "score": d.score,
            "attention_class": d.attention_class,
        }
        for d in data
    ]

    return processed
