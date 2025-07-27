import tensorflow as tf
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Text cleaning function
def clean(text):
    return ' '.join(''.join(char if char.isalpha() or char.isspace() else ' ' for char in text).split())

# Load the data
with open("Intent.json", "r") as f:
    data = json.load(f)

texts, labels, unique_intents = [], [], []

for intent_block in data["intents"]:
    intent = intent_block["intent"]
    if intent not in unique_intents:
        unique_intents.append(intent)
    for example in intent_block["text"]:
        texts.append(clean(example))
        labels.append(intent)

intent_to_index = {intent: i for i, intent in enumerate(unique_intents)}
index_to_intent = {i: intent for intent, i in intent_to_index.items()}

y_indices = [intent_to_index[label] for label in labels]

# Load the tokenizer
with open("tokenizer.json", "r") as f:
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(json.load(f))

# Prepare sequences
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, padding="pre")
categorical_labels = tf.keras.utils.to_categorical(y_indices, num_classes=len(unique_intents))

# Split test set
_, X_test, _, y_test = train_test_split(
    padded_sequences, categorical_labels, test_size=0.2, stratify=y_indices, random_state=42
)

# Load model
model = tf.keras.models.load_model("intent_model.keras")

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
print(f'\nTest Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

# Classification report
y_pred = np.argmax(model.predict(X_test), axis=1)
y_true = np.argmax(y_test, axis=1)

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=[index_to_intent[i] for i in sorted(np.unique(y_true))]))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(20, 20))
sns.heatmap(cm, cmap='Blues', annot=False, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
