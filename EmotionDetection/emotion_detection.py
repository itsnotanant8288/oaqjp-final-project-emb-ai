import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    output = {
    'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
    'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
    'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
    'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
    'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
    'dominant_emotion': dominant_emotion
    }
    if response.status_code == 400:
        output['anger']=None
        output['disgust']=None
        output['fear']=None
        output['joy']=None
        output['sadness']=None
        output['dominant_emotion']=None
        
    return output
