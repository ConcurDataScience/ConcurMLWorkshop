#!/bin/bash

# Start the TF Serving
exec tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=/app/model/ --model_name=model --enable_batching=true --batching_parameters_file="/app/tf-serving-batching-parameters.txt" &

# Start the Flask service
exec python3 /app/main.py