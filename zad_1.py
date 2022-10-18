class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f'Student {self.name}'

    @property
    def get_marks(self):
        return self.marks

    def is_passed(self):
        sum = 0
        marks = self.get_marks()
        for x in marks:
            sum+=x
        return sum/marks.len()>50


student1= Student("Gabriel", [100,90,20,30,40])
student2= Student("Andrzej", [100,0,20,30,40])
if (student1.is_passed):
    print(student1.__str__() + ' zdał')
if (student2.is_passed!=True):
        print(student2.__str__() + ' nie zdał')