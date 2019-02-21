# Armando Acosta
# CPSC 223P-03
# Simple project to emulate student record keeping

# Ask user how many students
numberStudents = int(input("How many students are in the school?\n"))
studentList = range(numberStudents)

# Initialize Dictionaries and Lists
schoolRosterList = []
classesList = []
courseDict = {}
classList = []

# Loop until all students are accounted for
for studentCount in studentList:
    # Initialize new student dictionaries/lists
    studentDict = {}
    studentCourseList = []
    studentGradeList = []

    studentDict["CWID"] = input("Enter new student's CWID.\n")
    studentDict["First Name"] = input("Enter student's name.\n")
    studentDict["Last Name"] = input("Enter student's last name.\n")
    studentDict["Gender"] = input("Enter student's gender.\n")
    studentDict["Birth-Date"] = input("Enter student D.O.B. in mm/dd/yyyy\n")
    studentDict["Enroll Date"] = input("Enter enrollment date.\n")

    # Course number check
    numberCourses = int(input("How many courses is the student enrolled in?\n"))
    courseList = range(numberCourses)
    print("Please enter class info in sequential order.\n")

    # Nested loop for list of courses student has
    for courseCount in courseList:
        studentCourse = input("Enter new course name.\n")
        studentGrade = input("What was the grade for the course?\n")
        studentCourseList.append(studentCourse)
        studentGradeList.append(studentGrade)

        if studentCourse in classesList:
            continue
        else:
            # Initialize dict key for class
            courseDict[studentCourse] = []
            classesList.append(studentCourse)

    # Creating student's course list to represent columns of course and grade
    studentDict["Course ID"] = studentCourseList
    studentDict["Grade"] = studentGradeList

    # Nested loop to check if student is enrolled in class
    for course in classesList:
        for studentEnroll in studentCourseList:
            if course == studentEnroll:
                # Adding student to class list
                classList = courseDict[course]
                classList.append(studentDict)
                courseDict[course] = classList

    schoolRosterList.append(studentDict)

print("All student info recorded successfully.")
