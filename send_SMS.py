from flask import Flask,request
import urllib
import psycopg2
import json

def indexsendSMS(request):
    message = request.json['message']
    mobile_number = request.json['mobile_number']
    authkey_msg91 = '195833ANU0xiap5a708d1f'
    country_code = request.json['country_code']
    sender_id = 'MSGIND'
    route = '4'
    

    url = 'http://api.msg91.com/api/sendhttp.php?country='+country_code+'&sender='+sender_id+'&route='+route+'&mobiles='+mobile_number+'&authkey='+authkey_msg91+'&message='+message
    

    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       test = str(the_page)
       test = test[2:-1]
       #test = json.loads(test)
    return json.dumps([{"Return_Value":test,"Return":"Sucess"}])
