import psycopg2
from datetime import datetime
import pandas as pd

class Book:

    def __init__(self):
        pass

    def connect_psycopg2(self):
        conn = psycopg2.connect(
            host = "localhost",
            database = "ola",
            user = "decagon",
            port = 5432    )
        
        # print(conn.get_dsn_parameters())
        
        return conn
        

    def get_all_users(self):
        
        try:
            conn = self.connect_psycopg2()
            # cursor = conn.cursor()
            # cursor.execute("SELECT * FROM books")
            # response = cursor.fetchall()
            select = ('SELECT * FROM books ORDER BY id;')
            table = pd.read_sql_query(select, conn)
            return table
        
        
        except Exception:
            "The table does not exist" 
        
        finally:
            if conn :
                conn.close()
    
    def get_by_user_id(self, user_id):
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE user_id = %s ", (user_id,))
            response = cursor.fetchall()
            return response
        
        except Exception:   
            return "User id not present in table 'Users' "
        
        finally:
            if conn :
                cursor.close()
                conn.close()
    
    def create_book_record(self, user_id, name, pages) :
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute(''' INSERT INTO books(user_id, name, pages)
                                VALUES(%s,%s,%s)''', (user_id, name, pages))
            conn.commit()
            return "Record created"
        
        except Exception:
            return "User id not present in table 'Users' "
        
        finally:
            if conn :
                cursor.close()
                conn.close()

    def get_by_id(self, num):
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM books WHERE id = %s ", (num,))
            response = cursor.fetchall()  
            return response  
        
        except Exception:
            return "User id not present in table 'Users' "
        
        finally:
            if conn :
                cursor.close()
                conn.close()

    def update_book_record(self, name, pages, id) :
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            
            updated_time = datetime.now()
            cursor.execute(''' UPDATE books
                            SET name = %s, pages = %s, updated_at = %s WHERE id = %s ''',
                                    (name, pages, updated_time, id)
            
                                    )
            conn.commit()
            return "Record updated"
        
        except Exception:
            return "Failed to update record "
        finally:
            if conn :
                cursor.close()
                conn.close()

    def delete_book_record(self, id):
        
        try:
            conn = self.connect_psycopg2()
            cursor = conn.cursor()
            cursor.execute(''' DELETE FROM books
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


    book = Book()
    # print(book.get_all_users())
    print(book.get_by_id(4))
    # print(book.create_book_record(1, 'Dark Ages', 70))
    # print(book.update_book_record("Na money be koko", 100, 4))
    # print(book.delete_book_record(9))
