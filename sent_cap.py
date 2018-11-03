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
     print(d)
     a = {k:v for k,v in d.items() if k not in ('key_id','key')}
     e = {k:v for k,v in d.items() if k  in ('key_id','key')}
     print(e)
     cus_date = datetime.datetime.utcnow()
     a['cus_date'] = cus_date 
     access =e['key_id']
     secret = e['key']
     sendforsentiment = sen_test(d['trans_text'],access,secret)
     a['sentiment'] = sendforsentiment
     print('asdf',a['sentiment'])
     gensql('insert', 'sentiment.sentimentcaps',a)
     return(json.dumps({'Status': 'Success','Message': 'Data Insert Sucessfully'},indent=4))
