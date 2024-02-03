from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

mydb = mysql.connector.connect(
   
    host = os.getenv('host'),
    user = os.getenv('user'),
    password = os.getenv('passwd') ,
    database = os.getenv('database')
)
cursor = mydb.cursor()

salle = cursor.execute("SELECT nom, capacite from salle; ")


results = cursor.fetchall() 

    
print(results)

cursor.close()
mydb.close()





