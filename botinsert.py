
import json
from datetime import datetime
from pytz import timezone
from sqlwrapperbot import gensql, dbget,dbput


def fun(request):
   d = request.json
   format = "%Y-%m-%d %H:%M:%S %Z%z"
   # Current time in UTC
   now_utc = datetime.now(timezone('UTC'))
   print(now_utc.strftime(format))
   # Convert to Asia/Kolkata time zone
   now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
   print(now_asia.strftime(format))
   d['custom_date'] = now_asia
   sql = gensql('insert','botschema.infocuit__website_table',d)
   print(sql)
   return(json.dumps({"Return":"Success","Status":200}))
    
