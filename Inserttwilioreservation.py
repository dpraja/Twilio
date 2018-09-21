from sqlwrapper import gensql,dbget,dbput
import json
import datetime
#from datetime 
import random
import urllib
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
    arr_date = datetime.datetime.strptime(data1, '%Y-%m-%d').date()
    dep_date = datetime.datetime.strptime(data2, '%Y-%m-%d').date()
    #print(type(data))
    restrict_days =  today_date + datetime.timedelta(days=90)
    print(restrict_days)
    #charges_end_date = datetime.datetime.strptime(data2, '%Y-%m-%d').date()
    #print("str2",charges_begin_date,charges_end_date,type(charges_end_date))
    
    if arr_date >= today_date:
        if  dep_date >= arr_date :    
            if dep_date <= restrict_days:
               sql_value = gensql('insert','reservation',d)
               return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Given dates are valid','ReturnCode':'Valid'}], sort_keys=True, indent=4))
            else:   
               return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'departure date should not exceed 90 days than arrival','ReturnCode':'Invalid'}], sort_keys=True, indent=4))
        else:
            
           return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Departure date should not be in past date than arrival','ReturnCode':'Invalid'}], sort_keys=True, indent=4))
    else:
        
         return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'arrival date must be scheduled atleast one day in advance','ReturnCode':'Invalid'}], sort_keys=True, indent=4))


def Modifytwilioreservation(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('confirmation_number')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('confirmation_number')}
    print(e)
    sql_value = gensql('update','reservation',a,e)
    print(sql_value)
    conf = e.get('confirmation_number')
    sql = dbput("update reservation set modification = 'yes' where confirmation_number = '"+conf+"'")
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}], sort_keys=True, indent=4))

def Canceltwilioreservation(request):
    d  = request.json
    conf = d.get('confirmation_number')
    status = 'Cancelled'

    sql = dbput("update reservation set status = '"+status+"' where confirmation_number = '"+conf+"'")
    print(sql)
    
    return(json.dumps([{'Status': 'Success', 'StatusCode': '200','Return': 'Your booking has been cancelled','ReturnCode':'RCS'}], sort_keys=True, indent=4))

def Smstwilioservice(request):
     countrycode = request.json['countrycode']
     #print(countrycode)
     name = "Customer"
     phone = request.json['mobile']
     message = request.json['message']
     conf_no = request.json['confirmation_number']
     hotel_name = 'dubakur hotel'
     arrival = request.json['arrival']
     depature = request.json['departure']
     room_type = request.json['roomtype']
     all_message = ("Dear "+name+", "+message+".  Confirmation Number is "+conf_no+", Arrival Date: "+arrival+", Depature Date:"+depature+", Room Type:"+room_type+". by "+hotel_name+"")
     url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+phone+"&message="+all_message+"&sender=Infoit&route=4&country="+countrycode+""
     req = urllib.request.Request(url)
     with urllib.request.urlopen(req) as response:
         the_page = response.read()
         the_page = the_page[1:]
         print(the_page)
         the_page = str(the_page)
     sql = dbput("update reservation set sms = 'success' where confirmation_number = '"+conf_no+"'")
     print(sql)
     return(json.dumps([{"Return":"SMS Sent Successfully","Return_Code":"SSS","Status": "Success","Status_Code": "200","Key":the_page}],indent =2))

 
