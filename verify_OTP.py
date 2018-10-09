from flask import Flask,request
import urllib
import psycopg2
import json

def indexverifyOTP(request):
    otp_num = request.json['otp_num']
    country_code=request.json['country_code']
    mobile_number = request.json['mobile_number']
    mobile=country_code + mobile_number
    print(mobile)
    authkey_msg91 = '195833ANU0xiap5a708d1f'
    

    url = 'https://control.msg91.com/api/verifyRequestOTP.php?authkey='+authkey_msg91+'&mobile='+mobile+'&otp='+otp_num
    
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       test = str(the_page)
       test = test[2:-1]
       test = json.loads(test)
    return json.dumps([(test)])
