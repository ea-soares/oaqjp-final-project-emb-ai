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
    return formatted_response
