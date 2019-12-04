from studentfile import StudentFileReader

FILE_NAME = "../students.txt"

def main():
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    studentList.sort(key = lambda rec: rec.idNum)
    printReport(studentList)

def printReport(theList):
    className = (None, "Freshman", "Sophomore", "Junior", "Senior")

    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' *4))

    for record in theList:
        print("%5d %-25s %-10s %4.2f" % \
              (record.idNum, \
               record.lastName + ', ' + record.firstName,
               className[record.classCode], record.gpa))

    print("- " * 50)
    print("Number of student:", len(theList))

main()
