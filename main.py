import sqlite3
import csv
import random


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

def generateAdvisor():
    facultyAdvisors = ["Maverick Deez", "Deez Nuts", "Nuts Deez", "Garlic Nubby", "Rex Plode"]
    advisorIndex = random.randint(0, 4)
    return facultyAdvisors[advisorIndex]
def makeWordsCorrectFormat(string):
    string_split = string.split(' ')
    result = []
    for word in string_split:
        result.append(word.capitalize())
    return ' '.join(result)

def splitZipCode(thing):
    splitUp = []
    for letter in thing:
        splitUp.append(letter)
    return splitUp



def isDeletedToZero():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE Student SET isDeleted = 0;")
        conn.commit()
        my_cursor.close()

def generateAdvisorsForWholeDB():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT StudentID FROM Student")
        student_ids = my_cursor.fetchall()
        for student_id in student_ids:
            advisor = generateAdvisor()
            my_cursor.execute(f"UPDATE Student SET FacultyAdvisor = '{advisor}' WHERE StudentID = {student_id[0]}")
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
                firstName = row['FirstName']
                FirstName = makeWordsCorrectFormat(firstName)
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
        firstName = input("Enter student's first name: ")
        FirstName = makeWordsCorrectFormat(firstName)
        lastName = input("Enter student's last name: ")
        LastName = makeWordsCorrectFormat(lastName)
        address = input("Enter student's address: ")
        Address = makeWordsCorrectFormat(address)
        city = input("Enter student's City: ")
        City = makeWordsCorrectFormat(city)
        while True:
            state = input("Enter student's State: ")
            State = makeWordsCorrectFormat(state)
            found = False
            for state in states:
                if state == State:
                    found = True
                    break # state is valid

            if found:
                break
            print("Invalid state. State should be of the Unites States.")
        while True:
            allDigits = True
            ZipCode = input("Enter student's ZipCode: ")

            for char in ZipCode:
                # If any character is not a digit, set allDigits to False and break the loop
                if not char.isdigit():
                    print("Invalid ZipCode, must be all digits")
                    allDigits = False
                    break

            # If all characters are digits, break the while loop
            if allDigits:
                break

        MobilePhoneNumber = input("Enter student's MobilePhoneNumber: ")
        FacultyAdvisor = generateAdvisor()
        major = input("Enter student's Major: ")
        Major = makeWordsCorrectFormat(major)
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
        isDeleted = 0
        my_cursor.execute(
            "INSERT INTO Student (FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,FacultyAdvisor,Major,GPA, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major, GPA, isDeleted))
        my_cursor.close()

def updateRecord():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        id = input("Please Enter the student ID of the student whose record you would like to update: ")
        id_int = int(id)
        numToUpdate = input("Please enter the number that corresponds with which action you would like to make: Enter 1 if you would like to update the student's major | 2 to update Advisor | 3 to update mobile phone number: \n")
        if numToUpdate == '1':
            new_major = input("Enter the student's new major: ")
            my_cursor.execute(f"UPDATE Student SET Major = '{new_major}' WHERE StudentID = {id_int}")
        elif  numToUpdate == '2':
            new_advisor = input("Enter the student's new Advisor: ")
            my_cursor.execute(f"UPDATE Student SET FacultyAdvisor = '{new_advisor}' WHERE StudentID = {id_int}")
        elif  numToUpdate == '3':
            new_number = input("Enter the student's new Mobile Phone Number: ")
            my_cursor.execute(f"UPDATE Student SET MobilePhoneNumber = '{new_number}' WHERE StudentID = {id_int}")
        else:
            print("You didn't listen to my directions.")
            updateRecord()
        my_cursor.close()
def deleteStudent():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        id = input("Please Enter the student ID of the student whose record you would like to delete: ")
        id_int = int(id)
        my_cursor.execute(f"UPDATE Student SET isDeleted = 1 WHERE StudentID = {id_int}")
        my_cursor.close()



def queryByFiveAfformentioned():
    conn = sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite')
    with sqlite3.connect('/Users/brainlesscrane/Documents/CPSC_408/StudentDB.sqlite') as conn:
        my_cursor = conn.cursor()
        numToUpdate = input("By which field would you like to display students record by? \nPlease enter the number that corresponds with the field.\n1. Major \n2. Advisor \n3. GPA \n4. City \n5. State  \nEnter here: ")
        if numToUpdate == '1':
            new_major = input("Enter the major you would like to display records by: ")
            new_major01 = makeWordsCorrectFormat(new_major)
            my_cursor.execute(f"SELECT * FROM Student WHERE Major = '{new_major01}'")
            records = my_cursor.fetchall()
            for record in records:
                if record[11] == 0:
                    print(record)
        elif numToUpdate == '2':
            new_advisor = input("Enter the advisor you would like to display records by: ")
            new_advisor01 = makeWordsCorrectFormat(new_advisor)
            my_cursor.execute(f"SELECT * FROM Student WHERE FacultyAdvisor = '{new_advisor01}'")
            records = my_cursor.fetchall()
            for record in records:
                if record[11] == 0:
                    print(record)
        elif numToUpdate == '3':
            gpa = input("Enter the GPA you would like to display records by: ")
            gpa01 = float(gpa)
            my_cursor.execute(f"SELECT * FROM Student WHERE GPA = {gpa01}")
            records = my_cursor.fetchall()
            for record in records:
                if record[11] == 0:
                    print(record)
        elif numToUpdate == '4':
            city = input("Enter the City you would like to display records by: ")
            city01 = makeWordsCorrectFormat(city)
            my_cursor.execute(f"SELECT * FROM Student WHERE City = '{city01}'")
            records = my_cursor.fetchall()
            for record in records:
                if record[11] == 0:
                    print(record)
        elif numToUpdate == '5':
            state = input("Enter the State you would like to display records by: ")
            state01 = makeWordsCorrectFormat(state)
            my_cursor.execute(f"SELECT * FROM Student WHERE State = '{state01}'")
            records = my_cursor.fetchall()
            for record in records:
                if record[11] == 0:
                    print(record)
        else:
            print("You didn't listen to my directions.")
            queryByFiveAfformentioned()
        my_cursor.close()

def menu():
    we_are_mobbing = True
    while we_are_mobbing:
        directorNum = input('WELCOME\nPlease enter the corresponding number for the action you would like to perform.\n1) Display all students and all of their attributes.\n2) Add a new student record.\n3) Update a student record.\n4) Delete a student record.\n5) Display students by Major, GPA, City, State and Advisor.\n6) Exit Application\nEnter here: ')
        if directorNum == '1':
            displayAllStudents()
        elif directorNum == '2':
            addNewStudentRecord()
        elif directorNum == '3':
            updateRecord()
        elif directorNum == '4':
            deleteStudent()
        elif directorNum == '5':
            queryByFiveAfformentioned()
        elif directorNum == '6':
            we_are_mobbing = False
        else:
            print('Please enter the corresponding number for the action')



#generateAdvisorsForWholeDB()

#isDeletedToZero()

"""
change your path to StudentDB and student.csv in my function readCSV_toDB
before uncommenting the method by the same name below
"""

#readCSV_toDB()

menu()