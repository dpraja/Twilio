from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from datetime import datetime, timedelta
import random
def Inserttwilioreservation(request):
    d = request.json
    
    roomtype = request.json['roomtype']
    confir = (random.randint(100000,999999))
    d['confirmation_number'] = confir
    d['modification'] = "No"
    d['status'] = "Reserved"
    d['roomtype'] = roomtype.title()
    sql = gensql('insert','public.reservation',d)
    print(sql)
    confirmation= d.get("confirmation_number")
    return(json.dumps([{"Return":"Record Inserted Succcessfully","Returncode":"RIS","Status":"Success","Statuscode":200,"confirmation_number":confirmation}],indent=2))

def InsertArrivalDeparture(request):
    n  = 90
    d = request.json
    print(d)
    #e = { k : v for k,v in d.items() if v = '' }       
    #print(e)
    today_date = datetime.datetime.utcnow().date()
    print(today_date)
    '''
    arrival = e['arrival']
    depature = e['departure']
    print(arrival,depature,type(arrival))
    arr_date = datetime.datetime.strptime(arrival, '%Y-%m-%d').date()
    dep_date = datetime.datetime.strptime(depature, '%Y-%m-%d').date()
    print("str1", arr_date,dep_date,type(arr_date))
    '''
    data1 = d.get('arrival')
    data2 = d.get('departure')
    restrict_days =  datetime.now() - timedelta(days=N)
    charges_begin_date = datetime.datetime.strptime(data1, '%Y-%m-%d').date()
    charges_end_date = datetime.datetime.strptime(data2, '%Y-%m-%d').date()
    print("str2",charges_begin_date,charges_end_date,type(charges_end_date))
    
    if data1 >= today_date :
        if  data2 >= data1 :    
            if restrict_days >= data1:
               sql_value = gensql('insert','reservation',d)
            return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Validated','ReturnCode':'Valid'}, sort_keys=True, indent=4))

        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Departure should not be before arrival','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Invalid','Please choose upcoming days arrival date':'Invalid'}, sort_keys=True, indent=4))


