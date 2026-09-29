import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload containing the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the output in the specified dictionary format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
