import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header)
    formatted_response=json.loads(response.text)
    print(response.status_code)
    if response.status_code==200:
        result = formatted_response['emotionPredictions'][0]['emotion']
        result['dominant_emotion'] = max(result, key=result.get)
    elif response.status_code == 400:
        result={
            'anger':None,
            'joy': None,
            'sadness': None,
            'fear':None,
            'disgust':None,
            'dominant_emotion':None
        }
    return result

if __name__ == '__main__':
    print(emotion_detector(''))