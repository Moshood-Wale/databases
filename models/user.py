import psycopg2
from datetime import datetime
import pandas as pd

class User:

    def __init__(self):
        pass

    def connect_psycopg2(self):
        conn = psycopg2.connect(
            host = "localhost",
            database = "decagon",
            user = "decagon",
            port = 5432    )
        
        # print(conn.get_dsn_parameters())
        
        return conn
        

    def all(self):
        
        try:
            conn = self.connect_psycopg2()
            # cursor = conn.cursor()
            # cursor.execute("SELECT * FROM users")
            # response = cursor.fetchall()
            # for lines in response:
            #     print(lines)
            select = ('SELECT * FROM users ORDER BY id;')
            table = pd.read_sql_query(select, conn)
            return table
        
        except Exception:
            "The table does not exist" 
        
        finally:
            if conn :
                conn.close()
    

    def get_by_id(self, id):
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s ", (id,))
            response = cursor.fetchall()
            
            return response
        
        except Exception:   
            return "User id not present in table 'Users' "
        
        finally:
            if conn :
                cursor.close()
                conn.close()
    
    def create_user_record(self, username, first_name, last_name) :
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute(''' INSERT INTO users(username, first_name, last_name)
                                VALUES(%s,%s,%s)''', (username,first_name,last_name))
            conn.commit()
            return "Record created"

        except Exception:   
            return "User id not present in table 'Users' "
        
        finally:
            if conn :
                cursor.close()
                conn.close()
    
    def update_user_record(self, username, first_name, last_name, id) :
        
        try:    
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            
            update_time = datetime.now()
            cursor.execute(''' UPDATE users
                            SET username = %s, first_name = %s, last_name = %s, updated_at = %s WHERE id = %s ''',
                            (username, first_name, last_name, update_time, id)
                                )
            conn.commit()
            return "Record updated"
       
        except Exception:   
            return "Failed to update record "
        
        finally:
            if conn :
                cursor.close()
                conn.close()

    
    def delete_user_record(self, id):
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute(''' DELETE FROM users
                                WHERE id = %s''', (id,))
            conn.commit()
            return "Record deleted"
        
        except Exception:   
            return "Failed to delete record "
        
        finally:
            if conn :
                cursor.close()
                conn.close()
        


if __name__ == '__main__':

    user = User()
    print(user.all())
    # print(user.get_by_id(3))
    # print(user.create_user_record("jacks9", "Allison", "Becker"))
    # print(user.update_user_record("mkd1", "Cleo", "Patra", 5))
    # print(user.delete_user_record(10))
