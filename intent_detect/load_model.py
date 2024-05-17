import tensorflow as tf
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
import numpy as np
import random
import json

import warnings

warnings.filterwarnings('ignore')

# Load the data
with open('Intent.json', 'r') as f:
    data = json.load(f)

# Load the tokenizer
with open('tokenizer.json', 'r') as f:
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(json.load(f))


def clean(line):
    cleaned_line = ''
    for char in line:
        if char.isalpha() or char.isspace():
            cleaned_line += char
        else:
            cleaned_line += ' '
    cleaned_line = ' '.join(cleaned_line.split())
    return cleaned_line


# List of unique intents
unique_intents = [intent['intent'] for intent in data['intents']]

# Map intents to numerical indices
intent_to_index = {intent: i for i, intent in enumerate(unique_intents)}
index_to_intent = {i: intent for intent, i in intent_to_index.items()}

# Load the trained model
model = tf.keras.models.load_model('intent_model.keras')


def recognize_intent(query):
    words = clean(query).split()
    sent_tokens = [tokenizer.word_index.get(word, tokenizer.word_index['<unk>']) for word in words]
    sent_tokens = pad_sequences([sent_tokens], maxlen=model.input_shape[1], padding='pre')
    pred = model.predict(sent_tokens)
    pred_class = np.argmax(pred, axis=1)[0]
    intent_data = data['intents'][pred_class]
    # Entity detection
    detected_entities = []
    for entity in intent_data['entities']:
        if entity in query.lower():
            detected_entities.append(entity)

    # Include detected entities in the intent_data
    intent_data['detected_entities'] = detected_entities
    return intent_data


print("Note: Enter 'quit' to break the loop.")
while True:
    query = input('You: ')
    if query.lower() == 'quit':
        break
    intent_data = recognize_intent(query)
    bot_response = random.choice(intent_data['responses'])
    print(f'Bot: {bot_response} -- Intent Data: {intent_data}')
    print()
