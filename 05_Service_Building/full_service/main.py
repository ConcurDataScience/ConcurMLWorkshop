import logging

from flask import Flask

from service.endpoints import predict
from service.utils import load_keras_model, load_keras_tokenizer

# Constants used by the service
_SERVICE_NAME = 'mlservice'
_SERVICE_HOST = '0.0.0.0'
_SERVICE_PORT = 8080
_MODEL_NAME = 'tweet_sentiment'
_MODEL_PATH = './model/v1'
_TOKENIZER_PATH = './model/v1/keras_tokenizer.json'


def create_flask_application(model, tokenizer) -> Flask:
    """Creates a Flask app instance with the /predict endpoint registered.

    :param model: The keras model instance
    :param tokenizer:  The keras tokenizer instance
    :return: A FLask application instance
    """
    if (not model) or (not keras_tokenizer):
        raise ValueError("Invalid parameters")

    # Create the Flask app instance
    app = Flask(_SERVICE_NAME)

    # Register the predict endpoint
    app.add_url_rule(
        rule='/predict',
        endpoint='predict',
        view_func=predict,
        methods=['POST'],
        defaults={
            'model': model,
            'tokenizer': tokenizer
        })

    # Returns the created Flask instance
    return app


# Entrypoint for the service
if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    logging.info("Loading the keras model")
    keras_model = load_keras_model(_MODEL_PATH)

    logging.info("Loading the keras tokenizer")
    keras_tokenizer = load_keras_tokenizer(_TOKENIZER_PATH)

    logging.info("Creating the Flask application")
    application = create_flask_application(model=keras_model,
                                           tokenizer=keras_tokenizer)

    logging.info("Starting the http service")
    application.run(host=_SERVICE_HOST, port=_SERVICE_PORT)
