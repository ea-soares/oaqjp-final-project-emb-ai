'''
Watson NLP Language utilities
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''# Emotion prediction function from Watson NLP Language'''

    # URL of the emotion prediction service
    base_url = 'https://sn-watson-emotion.labs.skills.network/'
    api_url = 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    url = base_url + api_url
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(
        url,
        json = myobj,
        headers=header,
        timeout=120)

    formatted_response = json.loads(response.text)

    # Reset scores and dominant emotion to None
    scores = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None
    }
    dominant_emotion = None

    # Check for an OK (200) status and update scores
    if response.status_code == 200:
        scores['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        scores['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        scores['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
        scores['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
        scores['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        #get dominant emotion
        dominant_emotion = max(scores, key= lambda x: scores[x])

    # Return results, none if sctatus code different from 200
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
