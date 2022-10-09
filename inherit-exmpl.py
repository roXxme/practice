# class Coder():        e.g, Containership
#     def __init__(self):
#         self.name = input('name_')
#         self.lang = input('lang_')
    
#     def show_det(self):
#         print("NAme :" + str(self.name))
#         print("Lang :" + str(self.lang))


# class Pythone():
#     def __init__(self):
#         self.Prof = Coder()
#     def profile(self):
#         self.Prof.show_det()


# hey = Pythone()
# hey.profile()

# class Numb():         inheritance
#     def __init__(self):
#         self.num = 9
    
#     def inc(self):
#         self.num += 1
#     def dec(self):
#         self.num -= 1
    
# class Newnum(Numb):
#     def __init__(self):
#         super().__init__()
#     def shoval(self):
#         print("value:" + str(self.num))

# n = Newnum()
# n.inc()
# n.inc()
# n.dec()
# n.shoval()

# Show result of student
class Result(): #check available students and new student 
    stud_marks = {"A":88, 'B':71, 'C':84,'D':95,'E':60,'F':89}
    def add_rslt(self, student, marks):
        self.student = input(student)
        self.marks = int(input(marks))
        self.stud_marks[self.student] = self.marks

    
class Student(Result):
    # def __init__(self):
    #     super().__init__()
    def sho_rslt(self, name):
        self.name = self.student
        if name in self.stud_marks:
            print(name , "got" , self.stud_marks[name] , "marksprint")

add = Student()
add.add_rslt("Name_", "Marks")
for s in ['A','B','D','F','H']:
    add.sho_rslt(s) 
