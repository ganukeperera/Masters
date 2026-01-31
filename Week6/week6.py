import sqlite3

class DBManager:

    STUDENT_SCHEMA = """
    CREATE TABLE IF NOT EXISTS students(
            student_id TEXT NOT NULL,
            student_name VARCHAR(50) NOT NULL,
            score TEXT NOT NULL,
"""

    def __init__(self):
        self.__connection = sqlite3.connect("Students.db")
        self.initialize_db()

    def initialize_db(self):
        curser = self.__connection.cursor()
        curser.execute(self.STUDENT_SCHEMA)
        self.__connection.commit()

    def add_


class MSE800Class:
    
    def __init__(self):
        self.__initialize_students()
        self.__initialize_marks()
        
    def __initialize_students(self):  
        self.__students = {"1": "Andrew",
                    "2": "Ben",
                    "3": "Carl", 
                    "4": "David", 
                    "5": "Emily"
        }
    
    def __initialize_marks(self):
        self.__mse_score = {"1": "90",
                    "2": "70", 
                    "3": "40", 
                    "4": "84", 
                    "5": "33"
                    } 
        
    def get_passed_students(self):
        result = {}

        for student_id, name in self.__students.items():
            score = int(self.__mse_score[student_id])
            if score > 50 :
                result[name] = score
        return result
    

def main():
    mse = MSE800Class()
    students = mse.get_passed_students()
    print(students)

if __name__ == "__main__":
    main()


class Student:

    def __init__(self, student_id: str, name: str):
        self.__student_id = student_id
        self.__name = name

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def name(self):
        return self.__name
    