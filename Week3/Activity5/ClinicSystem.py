import sqlite3
import os

def main():
    db_path = "clinic.db"

    # To have fresh start each time when running the code
    if os.path.exists(db_path):
        os.remove(db_path)

    # Manage database connection
    db = DatabaseHandler(db_path)

    # Do the Schema initialization
    schema = SchemaIntializer(db)
    schema.initizlise()

    # Seed sample data. 
    # Need to add new methods to seed data if more tables added in future
    seeder  = DataSeeder(db)
    seeder.seed_doctors()
    seeder.seed_patients()

    # Task 1 : List information of patients whose age > 65
    print("\n>>> Senior patients' full information:")
    patient_repo = PatientRepo(db)
    patients = patient_repo.get_senior_patients()
    for p in patients:
        print(f"Full Name: {p[1]}  {p[2]}, Age: {p[4]}, Phone No: {p[3]}")
    print()

    # Task 2 : Display the total number of doctors who specialise in ophthalmology
    doctor_repo = DoctorRepo(db)
    count = doctor_repo.get_doctor_count("ophthalmology")
    print(f"\n>>> Number of doctors specialised in Ophthalmology = {count}\n")

class DataSeeder:
    def __init__(self, db: DatabaseHandler):
        self.db = db

    def seed_doctors(self):
        doctors = [
            Doctor(1, "Will", "Young", "Dermatalogy", "022 573 5633", "will@gmail.com"),
            Doctor(2, "Josh", "English", "ophthalmology", "022 573 5633", "josh@gmail.com"),
            Doctor(3, "Pat", "Cummins", "caridiology", "022 573 5633", "pat@gmail.com"),
            Doctor(4, "Zak", "Crawley", "pediatric", "022 573 5633", "zak@gmail.com"),
            Doctor(5, "Caneron", "Green", "ophthalmology", "022 573 5633", "green@gmail.com")
        ]
        doctor_repo = DoctorRepo(self.db)
        doctor_repo.save(doctors)

    def seed_patients(self):
        patients = [
            Patient(1, "Andrew", "Russel", "020 575 3446", 48),
            Patient(2, "Stuart", "Board", "020 575 4255", 21),
            Patient(3, "Jamie", "Anderson", "020 575 7453", 73),
            Patient(4, "Ben", "Stokes", "020 575 9402", 34),
            Patient(5, "Sam", "Curren", "020 575 4432", 68)
        ]
        patient_repo = PatientRepo(self.db)
        patient_repo.save(patients)

class SchemaIntializer:
    def __init__(self,db: DatabaseHandler):
        self.db = db

    def initizlise(self):
        try:
            # create `doctor` table
            self.db.cur.execute("""
                            CREATE TABLE IF NOT EXISTS doctor(
                            doctor_id INTEGER PRIMARY KEY,
                            first_name VARCHAR NOT NULL,
                            last_name VARCHAR NOT NULL,
                            phone_number VARCHAR NOT NULL,
                            email VARCHAR NOT NULL,
                            specialisation VARCHAR NOT NULL
                            )
                            """)
            self.db.commit()
        
            # create `patient` table
            self.db.cur.execute("""
                            CREATE TABLE IF NOT EXISTS patient(
                            patient_id INTEGER PRIMARY KEY,
                            first_name VARCHAR NOT NULL,
                            last_name VARCHAR NOT NULL,
                            phone_number VARCHAR NOT NULL,
                            age INTEGER NOT NULL
                            )
                            """)
            self.db.commit()
        except sqlite3.Error as e:
            print(f"SQLite error occurred: {e}")

class DatabaseHandler:
    def __init__(self, db_path = "clinic.db"):
        self.connection = sqlite3.connect(db_path)
        self.cur = self.connection.cursor()

    def close(self):
        self.connection.close()
    
    def commit(self):
        self.connection.commit()
        

class Doctor():
    def __init__(self,id, first_name, last_name, specialisation, phone_no, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.specialisation = specialisation
        self.phone_no = phone_no
        self.email = email

class DoctorRepo():
    def __init__(self,db: DatabaseHandler):
        self.db = db

    def save(self,doctors: list[Doctor]):
        try:
            doctors = [(doc.id, doc.first_name, doc.last_name, doc.phone_no, doc.email, doc.specialisation) for doc in doctors]
            self.db.cur.executemany("INSERT INTO doctor VALUES (?, ?, ?, ?, ?, ?)", doctors)
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Sqlite error has ocurred: {e}")
        
    def get_doctor_count(self, specialised_in):
        try: 
            result = self.db.cur.execute("SELECT COUNT(doctor_id) FROM doctor WHERE specialisation = ? COLLATE NOCASE", (specialised_in,))
            (count,) = result.fetchone()
            return count
        except sqlite3.Error as e:
            print(f"Sqlite error has ocurred: {e}")

class Patient:
    def __init__(self, id, first_name, last_name, phone_number, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

class PatientRepo:
    def __init__(self, db:DatabaseHandler):
        self.db = db

    def save(self, patients: list[Patient]):
        try:
            data = [(patient.id, patient.first_name, patient.last_name, patient.phone_number, patient.age) for patient in patients]
            self.db.cur.executemany("INSERT INTO patient VALUES (?, ?, ?, ?, ?)", data)
            self.db.commit()
        except sqlite3.Error as e:
            print(f"Sqlite error has ocurred {e}")
        
    def get_senior_patients(self):
        try:
            result = self.db.cur.execute("SELECT * FROM patient WHERE age > 65 ORDER BY patient_id ASC")
            patients = result.fetchall()
            return patients
        except sqlite3.Error as e:
            print(f"Sqlite error has ocurred {e}")
        

if __name__ == "__main__":
    main()