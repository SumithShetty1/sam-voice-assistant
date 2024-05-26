import tensorflow as tf
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
import numpy as np
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

# Save the tokenizer for later use
with open('tokenizer.json', 'w') as f:
    json.dump(tokenizer.to_json(), f)

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

# Save the trained model
model.save('intent_model.keras')

# Test data
test_text_inputs = [
    "hello",
    "lock the system",
    "sleep mode",
    "sign out",
    "restart the system",
    "shut down the system",
    "stop",
    "wake up",
    "who are you",
    "who am I",
    "what are you",
    "what can you do",
    "thank you",
    "goodbye",
    "what are your hobbies",
    "do you dream",
    "what is the meaning of life",
    "are you a robot",
    "sorry",
    "have a good day",
    "exit",
    "day before yesterday",
    "yesterday",
    "yesterday day",
    "yesterday month",
    "yesterday year",
    "day after tomorrow",
    "tomorrow",
    "tomorrow day",
    "tomorrow month",
    "tomorrow year",
    "time and date",
    "time and day",
    "time and month",
    "time and year",
    "current time",
    "current hour day",
    "current hour month",
    "current hour year",
    "current hour",
    "current date",
    "current day",
    "current month",
    "current year",
    "yes",
    "no",
    "temperature in bangalore",
    "weather in bangalore",
    "turn on the internet",
    "turn off the internet",
    "open the setting",
    "press",
    "select all and copy",
    "open",
    "close",
    "close current application",
    "what is",
    "increase the volume",
    "decrease the volume",
    "unmute",
    "mute",
    "increase brightness",
    "decrease brightness",
    "set brightness to",
    "show action center",
    "hide action center",
    "turn on wi-fi in action center",
    "turn off wi-fi in action center",
    "show wi-fi networks in action center",
    "turn on bluetooth in action center",
    "turn off bluetooth in action center",
    "show bluetooth devices in action center",
    "turn on airplane mode in action center",
    "turn off airplane mode in action center",
    "turn on battery saver in action center",
    "turn off battery saver in action center",
    "turn on night light in action center",
    "turn off night light in action center",
    "turn on nearby share in action center",
    "turn off nearby share in action center",
    "turn on bluetooth in settings",
    "turn off bluetooth in settings",
    "show bluetooth devices in settings",
    "turn on airplane mode in settings",
    "turn off airplane mode in settings",
    "turn on night light in settings",
    "turn off night light in settings",
    "turn on do not disturb",
    "turn off do not disturb",
    "turn on nearby share in settings",
    "turn off nearby share in settings",
    "turn on wi-fi in settings",
    "turn off wi-fi in settings",
    "show wi-fi networks in settings",
    "turn on hotspot",
    "turn off hotspot",
    "turn on light mode",
    "turn off light mode",
    "turn on bluetooth",
    "turn off bluetooth",
    "show bluetooth devices",
    "turn on airplane mode",
    "turn off airplane mode",
    "turn on night light",
    "turn off night light",
    "turn on nearby sharing",
    "turn off nearby sharing",
    "turn on wi-fi",
    "turn off wi-fi",
    "show wi-fi networks",
    "take a photo",
    "camera take a photo",
    "start video",
    "scan barcode",
    "take screenshot",
    "take screenshot in snipping tool",
    "screen record",
    "screen record in snipping tool",
    "record audio",
    "create",
    "search windows",
    "google search",
    "youtube search",
    "spotify search",
    "linkedin search",
    "amazon search",
    "twitter search",
    "github search",
    "wikipedia search",
    "facebook search",
    "instagram search",
    "netflix search",
    "search",
    "file explorer search",
    "play",
    "on spotify play"
]

test_intents = [
    "greet",
    "system_control_lock",
    "system_control_sleep",
    "system_control_sign_out",
    "system_control_restart",
    "system_control_shutdown",
    "assistant_sleep",
    "wake_up",
    "assistant_name",
    "user_identity",
    "assistant_status",
    "assistant_capabilities",
    "thank_you",
    "goodbye",
    "hobbies",
    "dream",
    "meaning_of_life",
    "robot",
    "apology",
    "good_day",
    "exit",
    "day_before_yesterday",
    "yesterday_date",
    "yesterday_day",
    "yesterday_month",
    "yesterday_year",
    "day_after_tomorrow_date",
    "tomorrow_date",
    "tomorrow_day",
    "tomorrow_month",
    "tomorrow_year",
    "time_and_date",
    "time_and_day",
    "time_and_month",
    "time_and_year",
    "current_time",
    "current_hour_day",
    "current_hour_month",
    "current_hour_year",
    "current_hour",
    "current_date",
    "current_day",
    "current_month",
    "current_year",
    "yes",
    "no",
    "temperature",
    "weather",
    "internet_on",
    "internet_off",
    "open_settings",
    "keyboard_keys",
    "shortcut_keys",
    "open_application",
    "close_application",
    "close_current_window",
    "wikipedia",
    "volume_up",
    "volume_down",
    "unmute",
    "mute",
    "increase_brightness",
    "decrease_brightness",
    "set_brightness",
    "show_action_center",
    "hide_action_center",
    "on_wifi_action_center",
    "off_wifi_action_center",
    "show_wifi_networks_action_center",
    "on_bluetooth_action_center",
    "off_bluetooth_action_center",
    "show_bluetooth_devices_action_center",
    "on_airplane_mode_action_center",
    "off_airplane_mode_action_center",
    "on_battery_saver",
    "off_battery_saver",
    "on_night_light_action_center",
    "off_night_light_action_center",
    "on_nearby_sharing_action_center",
    "off_nearby_sharing_action_center",
    "on_bluetooth_settings",
    "off_bluetooth_settings",
    "show_bluetooth_devices_settings",
    "on_airplane_mode_settings",
    "off_airplane_mode_settings",
    "on_night_light_settings",
    "off_night_light_settings",
    "on_do_not_disturb",
    "off_do_not_disturb",
    "on_nearby_share_settings",
    "off_nearby_share_settings",
    "on_wifi_settings",
    "off_wifi_settings",
    "show_wifi_networks_settings",
    "on_hotspot",
    "off_hotspot",
    "on_light_dark_mode",
    "off_light_dark_mode",
    "on_bluetooth",
    "off_bluetooth",
    "show_bluetooth_devices",
    "on_airplane_mode",
    "off_airplane_mode",
    "on_night_light",
    "off_night_light",
    "on_nearby_sharing",
    "off_nearby_sharing",
    "on_wifi",
    "off_wifi",
    "show_wifi_networks",
    "take_photo",
    "camera_take_photo",
    "camera_start_video",
    "scan_barcode",
    "take_screenshot",
    "snipping_tool_take_screenshot",
    "screen_record",
    "snipping_tool_screen_record",
    "record_audio",
    "create_file",
    "search_windows",
    "search_google",
    "search_youtube",
    "search_spotify",
    "search_linkedin",
    "search_amazon",
    "search_twitter",
    "search_github",
    "search_wikipedia",
    "search_facebook",
    "search_instagram",
    "search_netflix",
    "search_bing",
    "search_file_explorer",
    "play_media",
    "play_media_spotify"
]
test_sequences = tokenizer.texts_to_sequences(test_text_inputs)
test_padded_sequences = pad_sequences(test_sequences, padding='pre')
test_labels = np.array([intent_to_index[intent] for intent in test_intents])
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes=output_dim)

loss, accuracy = model.evaluate(test_padded_sequences, test_labels)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
