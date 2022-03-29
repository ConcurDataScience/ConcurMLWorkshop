import json
import re

import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json


def load_keras_model(model_path):
    """Load the keras model in the memory.

    :param model_path: The path for the saved model folder.
    :return: A Keras model instance.
    """
    if not model_path:
        raise ValueError("Invalid model_path")

    return load_model(model_path)


def load_keras_tokenizer(tokenizer_path):
    """Load the tokenizer from a json file

    :param tokenizer_path: The file path for the keras tokenizer json file
    :return: Returns the keras tokenizer instance
    """
    if not tokenizer_path:
        raise ValueError("Invalid tokenizer_path")

    with open(tokenizer_path) as f:
        keras_tokenizer = tokenizer_from_json(json.load(f))
        return keras_tokenizer


def preprocess_tweet(tweet_text):
    """Clean the text from a tweet to make compatible with the model's input.

    :param tweet_text: The raw text from the tweet
    :return: The clean text.
    """
    stopwords = nltk.corpus.stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    tweet_text = re.sub('[^a-zA-Z]', ' ', tweet_text)
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.split()
    tweet_text = [lemmatizer.lemmatize(word) for word in tweet_text if
                  (not (word in set(stopwords))) & (len(word) > 1)]
    tweet_text = ' '.join(tweet_text)
    return tweet_text
