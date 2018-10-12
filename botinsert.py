
import json
from sqlwrapperbot import gensql, dbget,dbput


def fun(request):
   d = request.json
   sql = gensql('insert','botschema.infocuit__website_table',d)
   print(sql)
   return(json.dumps({"Return":"Success","Status":200}))
    
