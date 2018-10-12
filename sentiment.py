import boto3
import json
from flask import Flask,request
def sentiment(request):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
                
    message = request.json['message']

    print('Calling DetectSentiment')

    test=comprehend.detect_sentiment(Text=message,LanguageCode='en')['Sentiment']
    test_score=comprehend.detect_sentiment(Text=message,LanguageCode='en')['SentimentScore']
    result ={
            "Sentiment": test,
            "Sentiment_score" :test_score
        }
    print(json.dumps(result))
    return(json.dumps({result}))
    print('End of DetectSentiment\n')

    print ("Done")
