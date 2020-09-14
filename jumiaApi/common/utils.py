import os 

def apiResponse(status,message,responseData=[]):
    return { 
        "status": status,
         "msg": message,
         "responseData":responseData
    }