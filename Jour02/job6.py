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

salle = cursor.execute("SELECT SUM(capacite) FROM salle")


results = cursor.fetchall() 

    
print(f"La capacité de toutes les salles est de : {results[0][0]}")

cursor.close()
mydb.close()





