import json
import boto3
import datetime
from sqlwrapper_sentiment import gensql
#from check import sen_test

def sen_test(msg,access_key,secrete_key):

    print("hai")
    comprehend = boto3.client(service_name='comprehend',aws_access_key_id = access_key,aws_secret_access_key = secrete_key,region_name='us-east-1')
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

def sent(request):
     d = request.json
     #e = {k:v for k,v in d.items() if k not in ('sentiment')}
     cus_date = datetime.datetime.utcnow()
     d['cus_date'] = cus_date
     d['sentiment'] = sen_test(d['transcript_text'],d['aws_access_key_id'],d['aws_secret_key'])
     #d['aws_access_key'] = sen_test(d['aws_access_key_id'])
     #d['aws_secret_key'] = sen_test(d['aws_secret_key'])
     
     print('asdf',d['sentiment'])
     gensql('insert', 'sentiment.sentiment',d)
     return(json.dumps({'Status': 'Success','Message': 'Data Insert Sucessfully'},indent=4))
