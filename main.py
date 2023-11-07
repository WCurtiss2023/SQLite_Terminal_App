import sqlite3
import csv






def isDeletedToZero():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE Student SET isDeleted = 0;")
        conn.commit()
        my_cursor.close()




#my_cursor.execute("SELECT TrackId, Name FROM Track LIMIT 10;")

def readCSV_toDB(): #here is the function to read the csv file and insert the rows into the students file
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        with open('students.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
    # Iterate through CSV rows and insert into the SQLite database
            for row in csvreader:
                FirstName = row['FirstName']
                LastName = row['LastName']
                Address = row['Address']
                City = row['City']
                State = row['State']
                ZipCode = row['ZipCode']
                MobilePhoneNumber = row['MobilePhoneNumber']
                Major = row['Major']
                GPA = row['GPA']

                my_cursor.execute("INSERT INTO Student (FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,Major,GPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,Major,GPA))
   # Commit the changes and close the connection
            conn.commit()


#readCSV_toDB()
def displayFirstName():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()

     # Executing the SELECT query
        my_cursor.execute("SELECT DISTINCT FirstName FROM Student LIMIT 5;")

    # Fetching all records from the query result
        records = my_cursor.fetchall()

    # Displaying the records
        for record in records:
            print(record)

    # Closing the cursor
        my_cursor.close()

def displayAllStudents():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()

     # Executing the SELECT query
        my_cursor.execute("SELECT * FROM Student;")

    # Fetching all records from the query result
        records = my_cursor.fetchall()

    # Displaying the records
        for record in records:
            if record[11] == 0:
                print(record)

    # Closing the cursor
        my_cursor.close()

def addNewStudentRecord():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        FirstName = input("Enter student's first name: ")
        LastName = input("Enter student's last name: ")
        Address = input("Enter student's address: ")
        City = input("Enter student's City: ")
        State = input("Enter student's State: ")
        ZipCode = input("Enter student's ZipCode: ")
        MobilePhoneNumber = input("Enter student's MobilePhoneNumber: ")
        FacultyAdvisor = input("Enter student's Faculty Advisor: ")
        Major = input("Enter student's Major: ")
        while True:
            gpa_input = input("Enter GPA: ")
            try:
                GPA = float(gpa_input)
                if 0 <= GPA <= 4:
                    break  # Valid GPA, exit the loop
                else:
                    print("Invalid GPA. GPA should be between 0 and 4.")
            except ValueError:
                print("Invalid GPA input. Please enter a numeric value for GPA.")
        my_cursor.execute(
            "INSERT INTO Student (FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,FacultyAdvisor,Major,GPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major, GPA))
        my_cursor.close()


addNewStudentRecord()