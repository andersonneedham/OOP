from datetime import date


class Student:
    def __init__(self, StudentID, Name, DOB, Classification):
        self.StudentID = StudentID
        self.Name = Name
        self.DOB = DOB
        self.classification = Classification

    def calc_age(self):
        today = date.today()
        age = today.year - self.DOB.year
        return age
    
    def register_date(self):
        if self.classification == "Sr":
