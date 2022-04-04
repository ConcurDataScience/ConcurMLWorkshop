import os
import pandas as pd
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras.models import save_model
#from keras.models import save_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Bidirectional, LSTM
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json

max_words = 5000
max_len=50
keras_tokenizer = Tokenizer(num_words=max_words, lower=True, split=' ')


def train(input_file, output_folder):
    df = pd.read_csv(input_file)
    
    train_df, test_df = train_test_split(df,test_size = 0.05, random_state =42)

    train_df.reset_index(drop = True, inplace = True)
    test_df.reset_index(drop = True, inplace = True)

    X_train = train_df['tweet_text_preprocessed']
    y_train = train_df['sentiment']

    X_test = test_df['tweet_text_preprocessed']
    y_test = test_df['sentiment']

    keras_tokenizer.fit_on_texts(train_df['tweet_text_preprocessed'])
    train_texts_to_sequences = keras_tokenizer.texts_to_sequences(train_df['tweet_text_preprocessed'])
    train_texts_to_sequences = pad_sequences(train_texts_to_sequences, padding='post', maxlen=max_len)
    train_df['tweet_keras_tokenized'] = list(train_texts_to_sequences)

    test_texts_to_sequences = keras_tokenizer.texts_to_sequences(test_df['tweet_text_preprocessed'])
    test_texts_to_sequences = pad_sequences(test_texts_to_sequences, padding='post', maxlen=max_len)
    test_df['tweet_keras_tokenized'] = list(test_texts_to_sequences)
    
    keras_model = Sequential()
    embedding_vector_size = 16
    lstm_units = 20
    keras_model.add(Embedding(max_words,embedding_vector_size,input_length=max_len))
    #keras_model.add(Bidirectional(LSTM(20, return_sequences=True)))
    keras_model.add(Bidirectional(LSTM(lstm_units)))
    keras_model.add(Dense(4, activation='softmax'))
    keras_model.compile(
         loss='sparse_categorical_crossentropy',
         optimizer='adam',
         metrics=['accuracy'])
    
    X_train_keras = train_texts_to_sequences
    y_train_keras = train_df['sentiment_index']

    X_test_keras = test_texts_to_sequences
    y_test_keras = test_df['sentiment_index']

    keras_model.fit(
         X_train_keras, y_train_keras,
         validation_data=(X_test_keras, y_test_keras),
         epochs=1)
    
    save_model(keras_model, output_folder.rstrip('/') + '/', save_format='tf')

    print('DONE')
    #tokenizer_json =  keras_tokenizer.to_json()
    #with io.open(f'{current_path}/keras_model_files/keras_tokenizer.json', 'w', encoding='utf-8') as f:
    #    f.write(json.dumps(tokenizer_json, ensure_ascii=False))
    


if __name__ == "__main__":

    input_file = os.environ.get('SM_CHANNEL_TRAIN') + '/tweets_processed.csv'
    output_folder = os.environ.get('SM_MODEL_DIR') #os.path.join('/opt/ml/processing/output', 'tweets_processed.csv')

    #input_file = os.path.join('.', 'tweets_processed.csv')
    #output_folder = '.'
    
    print('Input', input_file)
    print('Output', output_folder)
       
    train(input_file, output_folder)
