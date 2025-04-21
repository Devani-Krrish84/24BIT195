students = [(1, "John", 20), (2, "Sophia", 22), (3, "David", 19), (4, "Emma", 21)]

def get_students(students) :
    
    roll_no = []
    name = []
    age = []

    for student in students :
        if isinstance(student, tuple) :
            roll_no.append(student[0])
            name.append(student[1])
            age.append(student[2])
        else :
            print("Invalid student data")
    return roll_no, name, age

roll_no, name, age = get_students(students)
print("Roll No:", roll_no)
print("Name:", name)
print("Age:", age)