from django.shortcuts import render
from manytomany_app.models import Student, Course

student1 = Student(name='John', age=20)
student1.save()

student2 = Student(name='Adil', age=21)
student2.save()

student3 = Student(name='Deniel', age=22)
student3.save()

course1 = Course(title='Python', description='Description 1')
course1.save()

course2 = Course(title='Html', description='Description 2')
course2.save()

course3 = Course(title='Django', description='Description 3')
course3.save()

course1.students_related.add(student1, student2)
course2.students_related.add(student2, student3)
course3.students_related.add(student1, student3)