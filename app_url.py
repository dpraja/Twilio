import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from Inserttwilioreservation import Inserttwilioreservation
from Inserttwilioreservation import InsertArrivalDeparture
app = Flask(__name__)
CORS(app)

@app.route('/Inserttwilioreservation',methods=['POST'])
def reservation():
   return Inserttwilioreservation(request)
@app.route('/InsertArrivalDeparture',methods=['POST'])
def InsertArrivalDeparture_all():
   return InsertArrivalDeparture(request)

if __name__ == "__main__":
  #app.run(debug=True)
  app.run(host="192.168.56.1",port=5000)
