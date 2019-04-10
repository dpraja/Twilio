import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from Inserttwilioreservation import Inserttwilioreservation
from Inserttwilioreservation import InsertArrivalDeparture
from Inserttwilioreservation import Modifytwilioreservation
from Inserttwilioreservation import Canceltwilioreservation
from Inserttwilioreservation import Smstwilioservice
from Inserttwilioreservation import CheckConfirmation
from Send_OTP import index
from verify_OTP import indexverifyOTP
from send_SMS import indexsendSMS
from txt_to_pdf import genpdf
#sentiment
from sentiment_insert import sentiment
from sent_cap import sent
#----------translator-----------#
from translator import translatortamil
#---------------------------------------------------
from botinsert import fun
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return ("Hello Twilio")

@app.route('/send_OTP',methods=['GET','POST'])
def indexotp():
   return index(request)

@app.route('/SMS_verify_OTP',methods=['GET','POST'])
def verify():
   return indexverifyOTP(request)

@app.route('/send_SMS_conf',methods=['POST'])
def sendSMS():
   return indexsendSMS(request)

@app.route('/getting_pdf',methods=['POST'])
def pdffun():
   return genpdf(request)

@app.route('/Inserttwilioreservation',methods=['POST'])
def reservation():
   return Inserttwilioreservation(request)
@app.route('/InsertArrivalDeparture',methods=['POST'])
def InsertArrivalDeparture_all():
   return InsertArrivalDeparture(request)

@app.route('/Modifytwilioreservation',methods=['POST'])
def Modifytwilioreservation_all():
   return Modifytwilioreservation(request)
@app.route('/Canceltwilioreservation',methods=['POST'])
def Canceltwilioreservation_all():
   return Canceltwilioreservation(request)
@app.route('/Smstwilioservice',methods=['POST'])
def Smstwilioservice_all():
   return Smstwilioservice(request)
@app.route('/CheckConfirmation',methods=['POST'])
def CheckConfirmation_all():
   return CheckConfirmation(request)
#----------------translator----------#

@app.route('/trans',methods=['POST'])
def Translator():
   return translatortamil(request)


#------------------------------------
@app.route("/infocuitchat",methods=['POST'])
def bot():
   return fun(request)

#sentiment

@app.route('/sentiment',methods=['POST'])
def test():
   return sentiment(request)

@app.route('/sentiment_cap',methods=['POST'])
def testing():
   return sent(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.1.29",port=5000)
