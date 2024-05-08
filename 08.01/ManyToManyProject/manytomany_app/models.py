from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', related_name='students', blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    students_related = models.ManyToManyField(Student, related_name='courses_related', blank=True, null=True)

    def __str__(self):
        return self.title