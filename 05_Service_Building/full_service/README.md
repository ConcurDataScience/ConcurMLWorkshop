# ML Service - Twitter Sentiment Analysis

This repository contains the implementation of service capable of predicting the sentiment of a tweet text.

## How to build the docker image
```shell
docker build . -t mlservice
```

## How to run the service
```shell
docker run -p 8080:8080 mlservice:latest
```

### Input Example
```json
{
    "text": "That was a great experience!"
}
```

### Output Example
```json
{
    "prediction": "Positive",
    "score": 0.3442407250404358
}
```
