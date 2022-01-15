#lambda with filter function
"""
l1=[78,98,38,47,5637]
final_list=list(filter(lambda x: (x%2)!=0,l1))
print(final_list)

lambda with map function
l1=[78,98,38,47,5637]
final_list=list(map(lambda x: x%2,l1))
print(final_list)

lambda with reduce function
from functools import reduce
l1=[78,98,38,47,5637]
sum=reduce(lambda x,y=x+y ,l1)
print(sum)"""
"""
OBJECT ORIENTED PROGRAMMING:
class Phone:
    def  set_color(self,color):
        self.color=color
    def show_color(self):
        return self.color
    def make_call(self):
        print('Calling')
    def play_game(self):
        print("playing game")

p1 = Phone()
p1.set_color("blue")
print(p1.show_color())
p1.make_call()
p1.play_game()
"""
#USING CONSTRUCTOR(__init__):
""""
class Student:
    def __init__(self,name,branch,pin_no,gend):
        self.name=name
        self.branch=branch
        self.pin_no=pin_no
        self.gend=gend
    def student_details(self):
        print('Student name:',self.name)
        print('Student branch:',self.branch)
        print('Student pin_no:',self.pin_no)
        print('Student gender:',self.gend)

s1= Student("Prashanth",'Electrical',207,'Male')
s1.student_details()

class new(Student):
    def show_det(self):
        print('I am child of Student')
s2=new('Hari',"Mechanical",305,'Male')
s2.show_det()
s2.student_details()

class Nothing(new):
    def no_ne(self):
        print('I am grand chiild of Stdent. And child of new.')
s3=Nothing('Mala','Cse',800,'Female')
s3.no_ne()
s3.student_details()
"""
#Overriding the parent class using SUPER() funcion
"""
class over(Student):
    def __init__(self, name, branch, pin_no, gend,location,Trans):
        super().__init__(name, branch, pin_no, gend)
        self.location=location
        self.Trans=Trans
    def over_det(self):
        print('Location:',self.location)
        print('Transport:',self.Trans)
s4=over('raghu','civil',120,'Male','Goplapatnam','RTC')
s4.over_det()
s4.student_details()
"""

#MULTIPLE INHERITENCE:
"""
class Par1:
    def par1(self,str1): 
        self.str1=str1
    def show_str1(self):
        return self.str1
class Par2:
    def par2(self,str2):
        self.str2=str2
    def show_str2(self):
        return self.str2
class Child(Par1,Par2):
    def chil(self,str3):
        self.str3=str3
    def show_str3(self):
        return self.str3
ch=Child()
ch.par1("I am string of parent 1")
ch.par2("I am string of parent 2")
ch.chil("I am string of child")
print(ch.show_str1())
print(ch.show_str2())
print(ch.show_str3())
"""
#parent child and grandchild inheritence:
"""
class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name
class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age
class Grandchild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender

gc=Grandchild()
gc.get_name("Raghu")
gc.get_age(15)
gc.get_gender("Male")
print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())
"""

