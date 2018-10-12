from flask import Flask,request
import urllib
import psycopg2
import random
import json
from sqlwrapper import gensql, dbget,dbput
app = Flask(__name__)
@app.route("/hello",methods=['POST'])

def fun(request):
   d = request.json
   sql = gensql('insert','botschema.infocuit__website_table',d)
   print(sql)
   return(json.dumps({"Return":"Success","Status":200}))
    
if __name__ == "__main__":
    app.run(host="192.168.1.7",port=5000)
