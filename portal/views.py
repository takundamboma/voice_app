from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "index.html")


def timetable(request):
    return render(request, "timetable.html")

def announcements(request):
    return render(request, "announcements.html")

def results(request):
    return render(request, "results.html")


from django.shortcuts import render
from .models import Announcement

def home(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, "index.html", {"announcements": announcements})

from django.shortcuts import render
from .models import Timetable

def timetable(request):
    timetable_entries = Timetable.objects.order_by("day", "time")
    return render(request, "timetable.html", {"timetable_entries": timetable_entries})

from django.shortcuts import render
from .models import Announcement, Result, Fee

def index(request):
    announcements = Announcement.objects.order_by('-date_posted')
    results = Result.objects.all()
    fees_list = Fee.objects.order_by('-date_updated')  # or any ordering you prefer

    return render(request, "index.html", {
        "announcements": announcements,
        "results": results,
        "fees_list": fees_list,
    })
def timetable(request):
    timetable_entries = Timetable.objects.order_by("day", "time")
    return render(request, "timetable.html", {"timetable_entries": timetable_entries})

def announcements(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, "announcements.html", {"announcements": announcements})

def results(request):
    results = Result.objects.order_by("-date_released")
    return render(request, "results.html", {"results": results})

from django.shortcuts import render
from .models import Fee

def fees(request):
    fees_list = Fee.objects.all()
    return render(request, "fees.html", {"fees_list": fees_list})

def home(request):
    announcements = Announcement.objects.order_by('-date_posted')
    fees_list = Fee.objects.all().order_by('-date_updated')
    return render(request, "index.html", {
        "announcements": announcements,
        "fees_list": fees_list
    })

# views.py
from django.shortcuts import render, redirect
from .models import ECounselingMessage, CounselingSession
from django.contrib.auth.decorators import login_required

@login_required
def ecounseling(request):
    student = request.user
    sessions = CounselingSession.objects.filter(student=student).order_by('-created_at')
    
    if request.method == "POST":
        message_text = request.POST.get("message")
        if message_text:
            ECounselingMessage.objects.create(student=student, message=message_text)
            return redirect('ecounseling')

    return render(request, "ecounseling.html", {"sessions": sessions})

from .models import ContinuousAssessment

def continuous_assessment(request):
    ca_list = ContinuousAssessment.objects.order_by("-date_added")
    return render(request, "continuous_assessment.html", {"ca_list": ca_list})

from django.shortcuts import render, redirect
from .models import Evaluation
from django.contrib import messages

def evaluation_form(request):
    if request.method == "POST":
        lecturer_name = request.POST.get("lecturer_name")
        student_name = request.POST.get("student_name")
        course_name = request.POST.get("course_name")
        rating = request.POST.get("rating")
        comments = request.POST.get("comments")

        Evaluation.objects.create(
            lecturer_name=lecturer_name,
            student_name=student_name,
            course_name=course_name,
            rating=rating,
            comments=comments
        )
        messages.success(request, "Your evaluation has been submitted successfully.")
        return redirect("evaluation_form")

    return render(request, "evaluation_form.html")

def lecturer_evaluations(request, lecturer_name):
    evaluations = Evaluation.objects.filter(lecturer_name=lecturer_name).order_by("-date_submitted")
    return render(request, "lecturer_evaluations.html", {"evaluations": evaluations, "lecturer_name": lecturer_name})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RegisteredStudent

def student_login(request):
    if request.method == "POST":
        reg_number = request.POST.get("reg_number")

        try:
            student = RegisteredStudent.objects.get(reg_number=reg_number)
            # store reg_number in session
            request.session["reg_number"] = student.reg_number
            request.session["full_name"] = student.full_name
            return redirect("index_page")
        except RegisteredStudent.DoesNotExist:
            messages.error(request, "Registration number not found. Please contact admin.")

    return render(request, "student_login.html")

def index_page(request):
    reg_number = request.session.get("reg_number")
    full_name = request.session.get("full_name")
    if not reg_number:
        return redirect("student_login")

    return render(request, "index.html", {"reg_number": reg_number, "full_name": full_name})

def profile_page(request):
    reg_number = request.session.get("reg_number")
    full_name = request.session.get("full_name")
    if not reg_number:
        return redirect("student_login")

    return render(request, "profile.html", {"reg_number": reg_number, "full_name": full_name})
