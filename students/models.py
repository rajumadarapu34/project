from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course}"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.score}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.date}"
