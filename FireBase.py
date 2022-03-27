from pyrebase import pyrebase
from datetime import datetime

config = {
  "apiKey": "AIzaSyANeiJJsYeZ6GvXLdtQxm3HEM3Hyzabz88",
  "authDomain": "bodgers-ec1f3.firebaseapp.com",
  "projectId": "bodgers-ec1f3",
  "databaseURL": "https://bodgers-ec1f3-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "bodgers-ec1f3.appspot.com",
  "messagingSenderId": "779851048240",
  "appId": "1:779851048240:web:ede14f1a31c041ab4114f5",
  "measurementId": "G-5WW4FJWX4R"
}




i = 1



firebase = pyrebase.initialize_app(config)

database = firebase.database()

while True:
    a = str(input("enter reg no"))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    s = "Truck"+str(i)
    

    data = {"Registration Number":a,"Time":dt_string }
    database.child("Data").child(s).set(data)
    i=i+1 