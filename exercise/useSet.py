from linearset import Set

smith = Set()
smith.add("CSCI-112")
smith.add("MATH-121")
smith.add("HIST-340")
smith.add("ECON-101")

roberts = Set()
roberts.add("POL-101")
roberts.add("ANTH-200")
roberts.add("CSCI-112")
roberts.add("ECON-101")

# same cources
if smith == roberts:
    print("same")
else:
    sameCourses = smith.intersect(roberts)
    if sameCourses.isEmpty() :
        print("not taking any of the same courses.")
    else:
        print("same courses is :")
        for course in sameCourses:
            print(course)

# unique Courses
print("unique: ")
uniqueCourses = smith.difference(roberts)
for course in uniqueCourses:
    print(course)
