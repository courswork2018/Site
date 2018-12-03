# -*- coding: utf-8 -*-
'''
Unsupervised Learning for Sentiment Analysis

Lexicon Models used:

- AFINN
- SentiWordNet
- VADER

'''

import pandas as pd
import numpy as np
from afinn import Afinn
import evaluation as ev
import preprocessing as pp

def predict_sentiment(text):
    # Load Model
    afn = Afinn(emoticons=True)
    score = afn.score(text) # sentiment polarity
    return score

def afinn_model():
    # start = time.time()    
    print("Loading Dataset")
    dataset = pd.read_csv(r'../../data/raw/movie_reviews.csv')
    
    # Get reviews and sentiments
    print("Get reviews and sentiment")
    reviews = np.array(dataset['review'])
    sentiments = np.array(dataset['sentiment'])

    # Get data and normalize test
    test_reviews = reviews[49900:]
    test_sentiments = sentiments[49900:]

    # Normalize
    print("Normalize")
    norm_test_reviews = pp.normalize_text(test_reviews)
    print("Normalize Done")
    sample_review_ids = [3, 5]

    # Load Model
    afn = Afinn(emoticons=True)

    # Make a prediction with model
    for review, sentiment in zip(test_reviews[sample_review_ids], test_sentiments[sample_review_ids]):
        print('REVIEW:', review)
        print('Actual Sentiment:', sentiment)
        print('Predicted Sentiment polarity:', afn.score(review))
        print('-'*60)
    
    return 0

def main():
    text = "This movie sucks! Don't go watch it"
    score = predict_sentiment(text=text)
    print("Score: " + str(score))
    if score > 1.0:
        print("Positive")
    else:
        print("Negative")

    return 0

if __name__ == '__main__':
    main()