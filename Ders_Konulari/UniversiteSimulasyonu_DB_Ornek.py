import sqlite3


class University:
    def __init__(self,name, country):
        self.name=name
        self.country=country
        self.status=True

        self.connectDatabase()

    def run(self):
        self.menu()

        choice = self.choice()
        if choice == 1:
            self.addStudent()
        if choice == 2:
            self.deleteStudent()
        if choice == 3:
            self.updateStudent()
        if choice == 4:
            while True:
                try:
                    orderby=int(input("1)All\n2)Faculty\n3)Department\n4)Type\n5)Status\n\nSelect : "))
                    if orderby<1 or orderby>5:
                        continue

                    break
                except ValueError:
                    print("Must be integer!")

            self.showAllStudents(orderby)
        if choice == 5:
            self.systemExit()

    def menu(self):
        print("***** {} Administration System *****".format(self.name))
        print("\n1)Add Student\n2)Delete Student\n3)Update Student\n4)Show All Students\n5)Exit\n")

    def choice(self):
        while True:
            try:
                process = int(input("Select : "))
                if process < 1 or process > 5:
                    print("Operation number must be between 1-5, please select correct number!")
                    continue

                break
            except ValueError:
                print("Operation is must be integer number. Please write correct type.")
        return process

    def addStudent(self):
        print("*** Student Information ***")
        name=input("Student's name : ").lower().capitalize()
        surname=input("Student's surname : ").lower().capitalize()
        faculty=input("Student's faculty : ").lower().capitalize()
        department=input("Student's department : ").lower().capitalize()
        stid=input("Student's ID : ").lower().capitalize()

        while True:
            try:
                typ=int(input("Student's Education Type : "))
                if typ<1 or typ>2:
                    print("Student's Education Type must be 1 or 2 .\n")
                    continue
                break
            except ValueError:
                print("Type must be integer (1 or 2)\n")
        status="Active"
        self.cursor.execute(
            "INSERT INTO students VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name,surname,faculty,department,stid,typ,status))
        self.connect.commit()
        print("The student named {} {} succesfully added".format(name,surname))

    def deleteStudent(self):
        self.cursor.execute("SELECT * FROM students")

        allStudents=self.cursor.fetchall()

        convertAllStr=lambda x: [str(y) for y in x]

        for i,j in enumerate(allStudents,1): #database'den çektiğimiz verileri düzgün bir şekilde 1'den itibaren yazdırsın
            print("{}){} ".format(i," ".join(convertAllStr(j))))

        while True:
            try:
                select=int(input("Select the student to be deleted: "))
                break
            except ValueError:
                print("Please write correct type(int")
        self.cursor.execute("DELETE FROM students WHERE rowid={}".format(select))
        self.connect.commit()
        print("\nStudent succesfully deleted")

    def updateStudent(self):
        self.cursor.execute("SELECT * FROM students")

        allStudents = self.cursor.fetchall()

        convertAllStr = lambda x: [str(y) for y in x]

        for i, j in enumerate(allStudents,
                              1):  # database'den çektiğimiz verileri düzgün bir şekilde 1'den itibaren yazdırsın
            print("{}){} ".format(i, " ".join(convertAllStr(j))))

        while True:
            try:
                select = int(input("\nSelect the student to be deleted: "))
                break
            except ValueError:
                print("Please write correct type(int")

        while True:
            try:
                updateSelect=int(input("1)Name\n2)Surname\n3)Faculty\n4)Department\n5)Student ID\n6)Education Type\n7)Status: "))

                if updateSelect<1 or updateSelect>7:
                    continue

                break

            except ValueError:
                print("It must be int!")

        operations = ["name","surname","faculty","department","stid","typ","status"]

        if updateSelect == 6:
            while True:
                try:
                    newValue=int(input("Enter the new value: "))
                    if newValue not in (1,2):
                        continue

                    break
                except ValueError:
                    print("Please, it must be integer!\n")
            self.cursor.execute("UPDATE students SET typ={} where rowid={}".format(newValue,select))
        else:
            newValue = input("Enter the new value: ")
            self.cursor.execute("UPDATE students SET {}='{}' where rowid={}".format(operations[updateSelect-1],newValue,select))

        self.connect.commit()
        print("Update Success!")


    def showAllStudents(self,by):
        if by == 1:
            self.cursor.execute("SELECT * FROM students")

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudents,1):
                print("{}){} ".format(i, " ".join(convertAllStr(j))))
        if by == 2:
            self.cursor.execute("SELECT faculty FROM students")

            faculties = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in faculties:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select= int(input("\nSelect : "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE faculty='{}'".format(faculties[select-1][1][0]))
            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudents, 1):
                print("{}){} ".format(i, " ".join(convertAllStr(j))))
        if by == 3:
            self.cursor.execute("SELECT department FROM students")

            departments = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in departments:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select= int(input("\nSelect : "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE department='{}'".format(departments[select-1][1][0]))
            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudents, 1):
                print("{}){} ".format(i, " ".join(convertAllStr(j))))
        if by == 4:
            self.cursor.execute("SELECT typ FROM students")

            typ = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in typ:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select= int(input("\nSelect : "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE typ={}".format(typ[select-1][1][0]))
            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudents, 1):
                print("{}){} ".format(i, " ".join(convertAllStr(j))))
        if by == 5:
            self.cursor.execute("SELECT status FROM students")

            status = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in status:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select= int(input("\nSelect : "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE status='{}'".format(status[select-1][1][0]))
            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i, j in enumerate(allStudents, 1):
                print("{}){} ".format(i, " ".join(convertAllStr(j))))


    def systemExit(self):
        self.status=False
    def connectDatabase(self):
        self.connect=sqlite3.connect("odtu.db")
        self.cursor=self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, surname TEXT, faculty TEXT, department TEXT, stid TEXT, typ INT, status TEXT)")
        self.connect.commit()

ODTU=University("Orta Dogu Teknik University","Turkey")
while ODTU.status:
    ODTU.run()
