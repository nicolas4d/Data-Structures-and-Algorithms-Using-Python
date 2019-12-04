from array import Array2D

gradeFile = open("../exam grades", "r")

numStudnets = int(gradeFile.readline())
numExams = int(gradeFile.readline())

examGrades = Array2D(numStudnets, numExams)

i = 0
for student in gradeFile:
    grades = student.split()
    for j in range(numExams):
        examGrades[i, j] = int(grades[j])
    i += 1

gradeFile.close()

for i in range(numStudnets):
    total = 0
    for j in range(numExams):
        total += examGrades[i,j]

    examAvg = total / numExams
    print("%2d:  %6.2f" % (i+1, examAvg))
