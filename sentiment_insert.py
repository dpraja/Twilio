import json
import boto3
import datetime
from sqlwrapper_sentiment import gensql
#from check import sen_test

def sen_test(msg):

    print("hai")
    comprehend = boto3.client(service_name='comprehend',aws_access_key_id = 'AKIAIYWT75QI3CGX6IEQ',aws_secret_access_key = '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',region_name='us-east-1')
    message = msg
    print('Calling DetectSentiment')
    test = comprehend.detect_sentiment(Text=message, LanguageCode='en')['Sentiment']
    #test_score = comprehend.detect_sentiment(Text=message, LanguageCode='en')['SentimentScore']
    '''
    result = {
        "Sentiment": test,
        #"Sentiment_score": test_score
    }
    '''
    #print(json.dumps(result))
    return (test)

def sentiment(request):
     d = request.json
     #e = {k:v for k,v in d.items() if k not in ('sentiment')}
     cus_date = datetime.datetime.utcnow()
     d['cus_date'] = cus_date
     d['sentiment'] = sen_test(d['transcript_text'])
     print('asdf',d['sentiment'])
     gensql('insert', 'sentiment.sentiment',d)
     return(json.dumps({'Status': 'Success','Message': 'Data Insert Sucessfully'},indent=4))
