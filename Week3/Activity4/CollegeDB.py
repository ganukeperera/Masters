import sqlite3
import os

def main():
    db_path = "college.db"

    # To have fresh start each time when running the code
    if os.path.exists(db_path):
        os.remove(db_path)

    db = DatabaseHandler(db_path)

    # SchemaInitializer reposible for create tables and seed sample data to tables
    initialiser = SchemaInitializer(db)
    initialiser.initialise()
    initialiser.seedSampleData()

    # Task 1 : show the number of students for MSE800 course
    enrollmentRepo = EnrollmentRepo(db)
    count = enrollmentRepo.getNumberOfStudentForCourse("MSE800")
    print(f"\n>>> Number of students enrolled for MSE800 course = {count}")

    # Task 2 : List all teachers name who are teaching MSE801
    print("\n>>> Teachers names who are teaching MSE801:")
    teachersRepo = TeachersRepo(db)
    teachers = teachersRepo.teachersFor("MSE801")
    for row in teachers:
        print(f"{row[0]}  {row[1]}")
    print()

    db.conn.close() #Close the DB connection at the end

# Student Entity class
class Student:
    def __init__(self,id, firstName, lastName, address, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email


class StudentsRepo:
    def __init__(self, db):
        self.db = db
    
    # Insert list of students in the DB
    def save(self, students):
        data = [(s.id, s.firstName, s.lastName, s.address, s.email) for s in students]
        self.db.cur.executemany("INSERT INTO student VALUES(?, ?, ?, ?, ?)", data)
        self.db.conn.commit()
        

class Teacher:
    def __init__(self, id, firstName, lastName, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

# Teachers repo responsible to run database queries related to Teachers
class TeachersRepo:
    def __init__(self, db):
        self.db = db
    # Insert list of teachers in the DB
    def save(self, teachers: list[Teacher]):
        try: 
            data = [(t.id, t.firstName, t.lastName, t.email) for t in teachers]
            self.db.cur.executemany("INSERT INTO teacher VALUES(?, ?, ?, ?)", data)
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

    # Select list of teachers for given course
    def teachersFor(self,courseId):
        try:
            res = self.db.cur.execute("Select teacher.firstName, teacher.lastName from courseInstructor INNER JOIN teacher ON courseInstructor.teacherId = teacher.teacherId where courseId = ?", (courseId,))
            rows = res.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

class Course:
    def __init__(self, id, name, description, credits):
        self.id = id
        self.name = name
        self.description = description
        self.credits = credits

class CourseRepo:
    def __init__(self, db):
        self.db = db
    
    def save(self, courses: list[Course]):
        try:
            data = [(c.id, c.name, c.description, c.credits) for c in courses]
            self.db.cur.executemany("INSERT INTO course VALUES(?, ?, ?, ?)", data)
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")


class Enrollment:
    def __init__(self, student: Student, course: Course):
        self.studentId = student.id
        self.courseId = course.id
    
class EnrollmentRepo:
    def __init__(self, db):
        self.db = db

    def save(self, enrollments: list[Enrollment]):
        try:
            data = [(e.studentId, e.courseId) for e in enrollments]
            self.db.cur.executemany("INSERT INTO enrollment values(?, ?)", data)
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

    # Select number of students enrolled to the given course
    def getNumberOfStudentForCourse(self, courseId):
        try:
            res = self.db.cur.execute(
                "SELECT COUNT(studentId) FROM enrollment WHERE courseId = ?",
                (courseId,)   # tuple required
            )
            (count,) = res.fetchone()
            return count
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

class CourseInstructor:
    def __init__(self, teacher: Teacher, course: Course):
        self.teacherId = teacher.id
        self.courseId = course.id
    
class CourseInstructorRepo:
    def __init__(self, db):
        self.db = db

    def save(self, courseInstructors: list[CourseInstructor]):
        try:
            data = [(i.teacherId, i.courseId) for i in courseInstructors]
            self.db.cur.executemany("INSERT INTO courseInstructor values(?, ?)", data)
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")


class DatabaseHandler:
    def __init__(self, dbName = "College.db"):
        self.conn = sqlite3.connect(dbName)
        self.cur = self.conn.cursor()

class SchemaInitializer: 
    def __init__(self, db):
        self.db = db

    def initialise(self):
        # create student table
        try:
            self.db.cur.execute("""
                CREATE TABLE IF NOT EXISTS student(
                    studentId INTEGER PRIMARY KEY,
                    firstName VARCHAR,
                    lastName VARCHAR,
                    address VARCHAR,
                    email VARCHAR
                )
            """)
            self.db.conn.commit()

            # create course table
            self.db.cur.execute("""
            CREATE TABLE IF NOT EXISTS course(
                    courseId VARCHAR PRIMARY KEY,
                    name VARCHAR,
                    description VARCHAR,
                    credits INTEGER
                ) 
            """)
            self.db.conn.commit()

            # create Teacher table
            self.db.cur.execute("""
                CREATE TABLE IF NOT EXISTS teacher(
                        teacherId INTEGER PRIMARY KEY,
                        firstName VARCHAR,
                        lastName VARCHAR,
                        email VARCHAR
                        )
            """)
            self.db.conn.commit()

            # create Enrollment table
            self.db.cur.execute("""
                CREATE TABLE IF NOT EXISTS enrollment(
                        studentId INTEGER NOT NULL,
                        courseId VARCHAR NOT NULL,
                        PRIMARY KEY (studentId, courseId),
                        FOREIGN KEY (studentId) REFERENCES student(studentID),
                        FOREIGN KEY (courseId) REFERENCES course(courseId)
                        )
            """)
            self.db.conn.commit()

            # create courseInstructor table
            self.db.cur.execute("""
                CREATE TABLE IF NOT EXISTS courseInstructor(
                        teacherId INTEGER NOT NULL,
                        courseId VARCHAR NOT NULL,
                        PRIMARY KEY (teacherId, courseId),
                        FOREIGN KEY (teacherId) REFERENCES teacher(teacherId),
                        FOREIGN KEY (courseId) REFERENCES course(courseId)
                        )
            """)
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

    # insert sample Data
    def seedSampleData(self):
        students = [
            Student(1, "Liam", "Anderson", "Mount Eden", "liam@gmail.com"),
            Student(2, "Emma", "Collins", "Mount Roskill", "emma@gmail.com"),
            Student(3, "Noah", "Mitchell", "Auckaland", "noah@gmail.com"),
            Student(4, "Ava", "Richardson", "Wellington", "ava@gmail.com"),
            Student(5, "Ethan", "Thompson", "Hamilton", "ethan@gmail.com")
        ]
        stRepo = StudentsRepo(self.db)
        stRepo.save(students)

        courses = [
            Course("MSE800", "Professional Software Engineering", "", 30),
            Course("MSE801", "Research Methods", "", 15),
            Course("MSE802", "Quantum Computing", "", 15),
        ]
        courseRepo = CourseRepo(self.db)
        courseRepo.save(courses)

        teachers = [
            Teacher(270001, "Tim", "Banne", "tim@gmail.com"),
            Teacher(270002, "Thomas", "Cutting", "thomas@gmail.com"),
            Teacher(270003, "Jeff", "Haris", "jeff@gmail.com"),
        ]
        teachersRepo = TeachersRepo(self.db)
        teachersRepo.save(teachers)

        enrollments = [
            Enrollment(students[0], courses[0]),
            Enrollment(students[1], courses[0]),
            Enrollment(students[2], courses[1]),
            Enrollment(students[3], courses[1]),
            Enrollment(students[4], courses[2]),
        ]
        enrollmentRepo = EnrollmentRepo(self.db)
        enrollmentRepo.save(enrollments)

        courseInstructor = [
            CourseInstructor(teachers[0], courses[0]),
            CourseInstructor(teachers[0], courses[1]),
            CourseInstructor(teachers[1], courses[0]),
            CourseInstructor(teachers[1], courses[1]),
            CourseInstructor(teachers[2], courses[2]),
        ]
        courseInstructorRepo = CourseInstructorRepo(self.db)
        courseInstructorRepo.save(courseInstructor)

 
if __name__ == "__main__":
    main()