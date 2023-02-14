import StudentClass as sc

studentid = 1001
name = "John"
dob = "10/15/2001"
classification = "junior"

student1 = sc.Student(studentid)

studentid.calc_age()

student1.register()

print("Student age is:", student1.return_age())

print("Student can register between:", student1.return_registration())
