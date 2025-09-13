from django.contrib import admin
from .models import Announcement, Timetable, Result

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "message", "date_posted")
    search_fields = ("title", "message")
    list_filter = ("date_posted",)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("course_name", "day", "time", "lecturer", "venue")
    search_fields = ("course_name", "lecturer", "venue")
    list_filter = ("day",)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("student_name", "course_name", "grade", "date_released")
    search_fields = ("student_name", "course_name")
    list_filter = ("date_released",)
from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ("student_name", "total_amount", "amount_paid", "amount_left", "is_registered", "date_updated")

# admin.py
from django.contrib import admin
from .models import ECounselingMessage, CounselingSession

@admin.register(ECounselingMessage)
class ECounselingMessageAdmin(admin.ModelAdmin):
    list_display = ('student', 'message', 'created_at', 'responded')
    list_filter = ('responded', 'created_at')
    actions = ['mark_as_responded']

    def mark_as_responded(self, request, queryset):
        queryset.update(responded=True)
    mark_as_responded.short_description = "Mark selected messages as responded"

@admin.register(CounselingSession)
class CounselingSessionAdmin(admin.ModelAdmin):
    list_display = ('student', 'admin_message', 'session_time', 'venue', 'created_at')
    list_filter = ('session_time',)

from django.contrib import admin
from .models import ContinuousAssessment

@admin.register(ContinuousAssessment)
class ContinuousAssessmentAdmin(admin.ModelAdmin):
    list_display = ("student_name", "course_name", "marks_obtained", "total_marks", "date_added")

from .models import Evaluation

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("lecturer_name", "student_name", "course_name", "rating", "date_submitted")
    list_filter = ("lecturer_name", "course_name", "rating")

from .models import RegisteredStudent

@admin.register(RegisteredStudent)
class RegisteredStudentAdmin(admin.ModelAdmin):
    list_display = ("reg_number", "full_name", "date_registered")
    search_fields = ("reg_number", "full_name")
