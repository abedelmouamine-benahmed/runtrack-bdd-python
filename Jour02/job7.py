from dotenv import load_dotenv
import os
import mysql.connector


class employe:

    def __init__(self):
        #chargement du .env
        load_dotenv()

        #connection base de donnée
        self.mydb = mysql.connector.connect(
        
            host = os.getenv('host'),
            user = os.getenv('user'),
            password = os.getenv('passwd') ,
            database = os.getenv('database1')
        )
        self.cursor = self.mydb.cursor()

    def create(self,last_name,name,salary,service):
        try:
            sql = "INSERT INTO employe (nom,prenom,salaire,id_service) VALUES (%s,%s,%s,%s) "
            values = (last_name,name,salary,service)
            
            self.cursor.execute(sql,values)
            print("Employe Added successfully !")
            self.mydb.commit()
                    
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()

    def read(self):
        try:
            sql = "SELECT * FROM employe"
            self.cursor.execute(sql)
            show_table = self.cursor.fetchall()
            for i in show_table:
                print (i)
            self.mydb.commit()
                    
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()
 
        
    def update(self,colonne,new_name,id):
        try:
            match(colonne):
                case 'nom':
                    sql = "UPDATE employe SET nom = %s WHERE id = %s"
                case 'prenom':
                    sql = "UPDATE employe SET prenom = %s WHERE id = %s"
                case 'id_service':
                    sql = "UPDATE employe SET id_service = %s WHERE id = %s"
                case _:
                    print('Column name no found')
            values = (new_name,id)
            self.cursor.execute(sql,values)
            self.mydb.commit()
            print("Employe updated successfully")
              
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()
    
    
    def delete(self,id):
        try:    
            sql = "DELETE FROM employe WHERE id = %s"
            self.cursor.execute(sql,(id,))
            self.mydb.commit()
            print("Employe deleted successfully")
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()

    def close_all(self):
        self.cursor.close()
        self.mydb.close()

employe_ = employe()

employe_.close_all(self)