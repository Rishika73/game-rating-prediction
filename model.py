import pickle
import numpy as np
import pandas as pd

def load_model():
    # Load the pre-trained model from a pickle file
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def preprocess_data(input_dict):
    # Convert dictionary to DataFrame
    input_data = pd.DataFrame([input_dict])

    # Initial column for all engine and SDK features set to 0
    engine_sdk_columns = [
        'engine gamemaker', 'engine renpy  sdk sdl', 'engine unity', 'engine unity  sdk curl',
        'engine unity  sdk oculusxrplugin  sdk openvr', 'engine unity  sdk openvr', 'engine unity  sdk photon',
        'engine unity  sdk steamworksnet  sdk curl',
        'engine unreal  sdk nvidia apex  sdk nvidia nsight aftermath  sdk nvidia physx  sdk oculusxrplugin  sdk openvr  sdk vorbis',
        'sdk nwjs  sdk nodejs'
    ]
    for col in engine_sdk_columns:
        input_data[col] = 0

    # Update the column based on 'engineSelect' from input_dict
    if 'engineSelect' in input_dict:
        selected_engine = input_dict['engineSelect']
        if selected_engine in engine_sdk_columns:
            input_data[selected_engine] = 1
        del input_data['engineSelect']

    # Convert specific numeric columns to integers or floats as appropriate, handling commas and conversion
    numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews',
                       'review_percentage', 'players_right_now', '24_hour_peak', 'all_time_peak']
    for col in numeric_columns:
        input_data[col] = input_data[col].replace(',', '', regex=True).astype(float)

    return input_data

def make_prediction(input_data):
    # Preprocess the data if it's not already preprocessed
    preprocessed_data = preprocess_data(input_data)

    # Load the model
    model = load_model()
    
    # Make a prediction
    prediction = model.predict(preprocessed_data)
    return prediction
