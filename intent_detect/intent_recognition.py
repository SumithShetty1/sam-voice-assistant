import tensorflow as tf
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
import numpy as np
import random
import json

import warnings

warnings.filterwarnings('ignore')

# Load the data
with open('Intent.json', 'r') as f:
    data = json.load(f)


def clean(line):
    cleaned_line = ''
    for char in line:
        if char.isalpha() or char.isspace():
            cleaned_line += char
        else:
            cleaned_line += ' '
    cleaned_line = ' '.join(cleaned_line.split())
    return cleaned_line


# List of intents and all text data to create a corpus
intents = []
unique_intents = []
text_input = []
response_for_intent = {}

for intent in data['intents']:
    if intent['intent'] not in unique_intents:
        unique_intents.append(intent['intent'])
    for text in intent['text']:
        text_input.append(clean(text))
        intents.append(intent['intent'])
    if intent['intent'] not in response_for_intent:
        response_for_intent[intent['intent']] = []
    for response in intent['responses']:
        response_for_intent[intent['intent']].append(response)

# Tokenize the text input
tokenizer = Tokenizer(filters='', oov_token='<unk>')
tokenizer.fit_on_texts(text_input)
sequences = tokenizer.texts_to_sequences(text_input)
padded_sequences = pad_sequences(sequences, padding='pre')

# Map intents to numerical indices
intent_to_index = {intent: i for i, intent in enumerate(unique_intents)}
index_to_intent = {i: intent for intent, i in intent_to_index.items()}
categorical_target = [intent_to_index[intent] for intent in intents]
categorical_vec = tf.keras.utils.to_categorical(categorical_target, num_classes=len(unique_intents))

# Model parameters
epochs = 100
embed_dim = 300
lstm_num = 50
output_dim = categorical_vec.shape[1]

# Build the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(len(tokenizer.word_index) + 1, embed_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(lstm_num, dropout=0.1)),
    tf.keras.layers.Dense(lstm_num, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(output_dim, activation='softmax')
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train the model
model.fit(padded_sequences, categorical_vec, epochs=epochs, verbose=1)

# Test data
test_text_inputs = ["hello", "is internet on", "system lock", "sleep", "tell me your name", "who am i"]
test_intents = ["Greet", "CheckInternet", "SystemControl", "AssistantSleep", "AssistantName", "UserIdentity"]
test_sequences = tokenizer.texts_to_sequences(test_text_inputs)
test_padded_sequences = pad_sequences(test_sequences, padding='pre')
test_labels = np.array([intent_to_index[intent] for intent in test_intents])
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=output_dim)

loss, accuracy = model.evaluate(test_padded_sequences, test_labels)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')


def response(sentence):
    words = clean(sentence).split()
    sent_tokens = [tokenizer.word_index.get(word, tokenizer.word_index['<unk>']) for word in words]
    sent_tokens = pad_sequences([sent_tokens], maxlen=padded_sequences.shape[1], padding='pre')
    pred = model.predict(sent_tokens)
    pred_class = np.argmax(pred, axis=1)[0]
    return random.choice(response_for_intent[index_to_intent[pred_class]]), index_to_intent[pred_class]


print("Note: Enter 'quit' to break the loop.")
while True:
    query = input('You: ')
    if query.lower() == 'quit':
        break
    bot_response, intent = response(query)
    print(f'Bot: {bot_response} -- Intent: {intent}')
    print()
