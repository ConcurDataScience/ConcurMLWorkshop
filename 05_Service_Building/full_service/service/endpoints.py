import numpy as np
from flask import request
from tensorflow.keras.preprocessing.sequence import pad_sequences

from service.utils import preprocess_tweet

# Max length used in the input for the Keras model
_MAX_LEN = 50


def predict(model, tokenizer):
    """Predicts the sentiment of a tweet text sent in the input.

    :param model: The keras model instance
    :param tokenizer:  The keras tokenizer instance
    :return: A API response and a status code
    """
    # Parse the input json into a dictionary
    input_data = request.get_json()

    # Check for the text field
    if 'text' not in input_data or not input_data['text']:
        return {'error': 'Invalid input. The text key can not be empty.'}, 400

    # Define the indexing for each possible label in a dictionary
    class_to_index = {
        "Neutral": 0,
        "Irrelevant": 1,
        "Negative": 2,
        "Positive": 3
    }

    # Creates a reverse dictionary
    index_to_class = dict((v, k) for k, v in class_to_index.items())
    ids_to_names = lambda n: [index_to_class.get(x) for x in n]

    # Preprocess the tweet text
    pre_tweet = [preprocess_tweet(input_data['text'])]
    predict_texts_to_sequences = tokenizer.texts_to_sequences(pre_tweet)
    predict_texts_to_sequences = pad_sequences(predict_texts_to_sequences,
                                               padding='post',
                                               maxlen=_MAX_LEN)

    # Execute the inference
    keras_predictions = model.predict(predict_texts_to_sequences)

    # Post-process the model prediction and prepare the API response
    best_prediction_idx = np.argmax(keras_predictions, axis=1)
    best_prediction_label = ids_to_names(best_prediction_idx)
    result = {
        "prediction": best_prediction_label[0],
        "score": float(keras_predictions[0][best_prediction_idx])
    }

    return result, 200
