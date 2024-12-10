# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.index = 102983

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.index = 123456
    student2.name = "Daquira"
    student2.age = 21
    student2.index = 234567
    student3.name = "Carolina"
    student3.age = 20
    student3.index = 345678

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, index:{student1.index}')
    print(f'{student2.name}, {student2.age} years old index:{student2.index}')
    print(f'{student3.name}, {student3.age} years old index:{student3.index}')
 

if __name__ == "__main__":
    main()