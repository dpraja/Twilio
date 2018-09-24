import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from Inserttwilioreservation import Inserttwilioreservation
from Inserttwilioreservation import InsertArrivalDeparture
from Inserttwilioreservation import Modifytwilioreservation
from Inserttwilioreservation import Canceltwilioreservation
from Inserttwilioreservation import Smstwilioservice
from Inserttwilioreservation import CheckConfirmation
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return ("Hello Twilio")

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
if __name__ == "__main__":
  #app.run(debug=True)
  app.run(host="192.168.56.1",port=5000)
