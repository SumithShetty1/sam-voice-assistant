import tensorflow as tf
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import warnings

warnings.filterwarnings('ignore')

# Load intents from file
with open('Intent.json', 'r') as f:
    data = json.load(f)

# Text cleaning function
def clean(text):
    return ' '.join(''.join(char if char.isalpha() or char.isspace() else ' ' for char in text).split())

# Prepare training data
text_input, intents = [], []
response_for_intent = {}
unique_intents = []

for intent_block in data['intents']:
    intent = intent_block['intent']
    if intent not in unique_intents:
        unique_intents.append(intent)

    for text in intent_block['text']:
        text_input.append(clean(text))
        intents.append(intent)

    response_for_intent.setdefault(intent, []).extend(intent_block['responses'])

# Tokenization
tokenizer = Tokenizer(filters='', oov_token='<unk>')
tokenizer.fit_on_texts(text_input)
sequences = tokenizer.texts_to_sequences(text_input)
padded_sequences = pad_sequences(sequences, padding='pre')

# Save tokenizer
with open('tokenizer.json', 'w') as f:
    json.dump(tokenizer.to_json(), f)

# Encode intent labels
intent_to_index = {intent: idx for idx, intent in enumerate(unique_intents)}
index_to_intent = {idx: intent for intent, idx in intent_to_index.items()}

categorical_target = [intent_to_index[intent] for intent in intents]
categorical_vec = tf.keras.utils.to_categorical(categorical_target, num_classes=len(unique_intents))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, categorical_vec, test_size=0.2, random_state=42, stratify=categorical_target
)

# Model hyperparameters
embed_dim = 300
lstm_units = 50
epochs = 100
output_dim = len(unique_intents)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=embed_dim),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(lstm_units, dropout=0.1)),
    tf.keras.layers.Dense(lstm_units, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(output_dim, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# Train the model
model.fit(X_train, y_train, validation_split=0.1, epochs=epochs, verbose=1)

# Save trained model
model.save('intent_model.keras')

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
print(f'\nTest Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

# Generate predictions for classification report
y_pred = np.argmax(model.predict(X_test), axis=1)
y_true = np.argmax(y_test, axis=1)

print("\nClassification Report:\n")
labels = sorted(np.unique(y_true))  # only the classes that appear in y_true
target_names_filtered = [index_to_intent[i] for i in labels]
print(classification_report(y_true, y_pred, labels=labels, target_names=target_names_filtered))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(20, 20))
sns.heatmap(cm, annot=False, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
