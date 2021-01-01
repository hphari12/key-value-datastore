Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import threading
from threading import*
import time
d={}
#for creating datastore
#key - string and less than 32 chars
#value - json object and less than 16KB
#datastore - less than 1GB
def create(key,value,expTime=0):
    if key in d:
        print("Key already exists")
    else:
        if key.isalpha() and len(key)<=32:
            if len(d)< 2^30 and len(value)<=(16*(2^10)):  
                if expTime==0:
                    l=[value,expTime]
                else:
                    l=[value,time.time()+expTime]
                d[key]=l
            else:
                print("Memory limit exceeded")
        else:
            print("Invalid Key: Key must be alphabet and less than 32 chars")
#for reading datastore with key          
def read(key):
    if key in d:
        l=d[key]
        if l[1]!=0:
            if time.time()<l[1]:#comparing present time and expiry time
                return l[0]                
            else:
                print("Key expired")
        else:
            return l[0]
    else:
        print("Key not found")    
#for deleting key in datastore
def delete(key):
    if key in d:
        l=d[key]
        if l[1]!=0:
            if time.time()<l[1]:
                d.pop(key)
                print("Deleted successfully")
            else:
                print("Key expired")
    else:
        print("Key not found")
