import os
import pandas as pd
import re
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install('nltk')
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
stopwords = nltk.corpus.stopwords.words('english')


def preprocess_tweet(tweet_text):
    tweet_text = re.sub('[^a-zA-Z]', ' ', tweet_text)
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.split()
    tweet_text = [lemmatizer.lemmatize(word) for word in tweet_text if not word in set(stopwords)]
    tweet_text = ' '.join(tweet_text)
    return tweet_text


def main(input_file, output_file):
    df = pd.read_csv(input_file)
    df['tweet_text_preprocessed'] = df.apply(lambda x: preprocess_tweet(x['tweet_text']), axis=1)
    df = df[df.tweet_text_preprocessed.apply(lambda text: len(text.split())>1)]
    df.to_csv(output_file, index=False)

    
if __name__ == "__main__":

    input_file = os.path.join('/opt/ml/processing/input', 'tweets.csv')
    output_file = os.path.join('/opt/ml/processing/output', 'tweets_processed.csv')
    #input_file = os.path.join('.', 'tweets.csv')
    #output_file = os.path.join('.', 'tweets_processed.csv')
    
    main(input_file, output_file)
