from flask import Flask,request
import urllib
import psycopg2
import random
import json


def index(request):
    if request.method == 'GET':
        country_code=request.args['country_code']
        mobile_number = request.args['mobile_number']
        print(country_code)
    if request.method == 'POST':
        country_code=request.json['country_code']
        mobile_number = request.json['mobile_number']
        print(country_code)
    if country_code.find('+') != -1:
        pass
    else:
        country_code = '+'+country_code
    print("country_code", country_code)
    
    
    mobile=country_code + mobile_number
    authkey_msg91 = '195833ANU0xiap5a708d1f'
    c = random.randint(0,999999)
    print(c)
    otp_generate = str(c)
    
    url = 'http://control.msg91.com/api/sendotp.php?&authkey='+authkey_msg91+'&message=Your verification code is '+otp_generate+'&sender=OTPSMS&mobile='+mobile+'&otp='+otp_generate

    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       test = str(the_page)
       test = test[2:-1]
       test = json.loads(test)
    return json.dumps([(test)])
    

    


   
