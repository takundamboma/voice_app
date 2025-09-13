from django.db import models

# Create your models here.

from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class Timetable(models.Model):
    course_name = models.CharField(max_length=200)
    day = models.CharField(max_length=20)   # e.g. Monday
    time = models.CharField(max_length=50)  # e.g. 10:00 - 12:00
    lecturer = models.CharField(max_length=200, blank=True, null=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_name} on {self.day} at {self.time}"
class Result(models.Model):
    student_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=5)
    date_released = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name} ({self.grade})"

from django.db import models

class Fee(models.Model):
    student_name = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_updated = models.DateTimeField(auto_now=True)

    def amount_left(self):
        return self.total_amount - self.amount_paid

    def is_registered(self):
        return self.amount_paid >= (self.total_amount / 2)

    def __str__(self):
        return f"{self.student_name} - {'Registered' if self.is_registered() else 'Not Yet Registered'}"

# models.py
from django.db import models
from django.contrib.auth.models import User

class ECounselingMessage(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.student.username} at {self.created_at}"

class CounselingSession(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_message = models.TextField()
    session_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session for {self.student.username} at {self.session_time}"

class ContinuousAssessment(models.Model):
    student_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name} ({self.marks_obtained}/{self.total_marks})"

class Evaluation(models.Model):
    lecturer_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    rating = models.IntegerField(choices=[(1, "Poor"), (2, "Fair"), (3, "Good"), (4, "Very Good"), (5, "Excellent")])
    comments = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} → {self.lecturer_name} ({self.rating})"
from django.db import models

class RegisteredStudent(models.Model):
    reg_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=200)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reg_number} - {self.full_name}"
