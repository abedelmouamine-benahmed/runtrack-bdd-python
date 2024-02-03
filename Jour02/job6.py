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

salle = cursor.execute("SELECT * FROM salle")


results = cursor.fetchall() 

    
print(f"la capacité de toutes les salles est de : {results}")

cursor.close()
mydb.close()





