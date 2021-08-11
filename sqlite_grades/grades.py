
import sqlite3
import csv

class Grades:
    
    conn = sqlite3.connect("gradedb.sqlite")
    
    cursor = conn.cursor()


    def read_csv_file(self):
        with open('grades.csv', 'r') as file:
            dict_reader = csv.DictReader(file)
            to_database = [(i['Last name'], i['First name'], i['SSN'], i['Test1'],
                            i['Test2'], i['Test3'], i['Test4'], i['Final'],i['Grade']) for i in dict_reader]

            return to_database
          
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE if not exists students 
                               ('Last name' VARCHAR,
                               'First name' VARCHAR,
                                SSN VARCHAR,
                                Test1 REAL, Test2 REAL, Test3 REAL, Test4 REAL, 
                                Final REAL, Grade VARCHAR);''')

        self.conn.commit()
    
    def insert_into_table(self):
        self.cursor.executemany('''INSERT INTO students ('Last name', 
                                'First name', SSN, Test1, Test2, Test3, Test4, Final, Grade)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''', self.read_csv_file())
        self.conn.commit()

    
    def create_students_record(self,first_name,last_name,ssn,test1,test2,test3,test4,final,grade):
            
            self.cursor.execute('''INSERT INTO students ('Last name', 'First name', SSN, Test1, Test2, Test3, Test4, Final, Grade) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',(first_name,last_name,ssn,test1,test2,test3,test4,final,grade))
            self.conn.commit()
            
    def update_student(self,test1,test2,test3,test4,final,grade,ssn):
        
        self.cursor.execute('''UPDATE students
                        SET 'First name'= ?, SSN= ?, Test1= ?, Test2= ?, Test3= ?, Test4=?, Final=?, Grade=?
                        WHERE SSN=?
                         ''',(test1,test2,test3,test4,final,grade,ssn))
        
        self.conn.commit()
    


    def all(self):
        test = self.cursor.execute('SELECT * FROM students').fetchall()
        for row in test:
            print(row)
        return test
        
    def del_student_record(self,SSN):
        self.cursor.execute('DELETE FROM students where SSN=?',(SSN,))
        
    def student_that_passed(self):
        check = self.cursor.execute("SELECT * FROM students WHERE Final >= 50 ").fetchall()
        for row in check:
            print(row)
        return check
    
    def student_that_failed(self):
        check = self.cursor.execute("SELECT * FROM students WHERE Final<50 ").fetchall()   
        for row in check:
            print(row)
        return check
    
    def student_test1(self):
        check = self.cursor.execute("SELECT * FROM students WHERE Test1 > 45.0 ").fetchall() 
        for row in check:
            print(row)
        return check


if __name__ == '__main__':
    
    grade = Grades()
    # grade.create_table()
    # grade.insert_into_table()
    
    # grade.all()
    # grade.student_that_passed()
    # grade.student_that_failed()
    grade.student_test1()