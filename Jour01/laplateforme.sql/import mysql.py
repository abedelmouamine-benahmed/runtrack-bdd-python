import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lolo123009",
    database = "Laplateforme"
)
cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiant")
results = cursor.fetchall() 
print(results)

cursor.close()
mydb.close()