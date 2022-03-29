import json
import re

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# This can be replaced with the model location
max_len = 50
negative_tweet_text = 'i had an very sick bad service'
positive_tweet_text = 'i had an excellent service'

# Define the indexing for each possible label in a dictionary
class_to_index = {"Neutral": 0, "Irrelevant": 1, "Negative": 2, "Positive": 3}

# Creates a reverse dictionary
index_to_class = dict((v, k) for k, v in class_to_index.items())

ids_to_names = lambda n: np.array([index_to_class.get(x) for x in n])

def preprocess_tweet(tweet_text):
    tweet_text = re.sub('[^a-zA-Z]', ' ', tweet_text)
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.split()
    tweet_text = [lemmatizer.lemmatize(word) for word in tweet_text if
                  (not (word in set(stopwords))) & (len(word) > 1)]
    tweet_text = ' '.join(tweet_text)
    return tweet_text


with open('../model/v1/keras_tokenizer.json') as f:
    data = json.load(f)
    keras_tokenizer = tokenizer_from_json(data)

reconstructed_keras_model = load_model('../model/v1/')

preprocessed_tweet = [preprocess_tweet(tweet_text) for tweet_text in
                      [negative_tweet_text, positive_tweet_text]]

predict_texts_to_sequences = keras_tokenizer.texts_to_sequences(
    preprocessed_tweet)
predict_texts_to_sequences = pad_sequences(predict_texts_to_sequences,
                                           padding='post',
                                           maxlen=max_len)

keras_predictions = np.argmax(
    reconstructed_keras_model.predict(predict_texts_to_sequences), axis=1)

keras_prediction_labels_test = ids_to_names(keras_predictions)

print(keras_prediction_labels_test)
