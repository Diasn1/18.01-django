from django.core.management.base import BaseCommand
from manytomany_app.models import Student, Course

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('List of courses for each student:')
        for student in Student.objects.all():
            self.stdout.write(f'{student.name}: {student.courses.all()}')

        self.stdout.write('')
        self.stdout.write('List of students for each course:')
        for course in Course.objects.all():
            self.stdout.write(f'{course.title}: {course.students_related.all()}')