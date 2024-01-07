from django.shortcuts import render, redirect
from lecture.models import Lecture, Video
from .models import Calendar
from .forms import CalendarModelForm
from datetime import timedelta

def index(request):

    subject = request.GET.get('subject')

    lectures = Lecture.objects.filter(
        subject=subject) if subject else Lecture.objects.all()
    lectures = lectures.order_by('-student_count')
    for lecture in lectures:
        videos = Video.objects.filter(lecture=lecture)
        for video in videos:
            lecture.remain_time += video.video_duration
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)


def realhome(request):
    if request.method == 'POST':
        calendar = Calendar()
        calendar.author = request.user
        calendar.title = request.POST['eventTitle']
        calendar.label = request.POST['eventLabel']
        calendar.startdate = request.POST['eventStartDate']
        calendar.enddate = request.POST['eventEndDate']
        calendar.save()
        return redirect('realhome')
    cal = Calendar.objects.filter(author=request.user)
    for c in cal:
        c.enddate = c.enddate+timedelta(days=1)
        if c.label == '강의':
            c.label='blue'
        elif c.label == '복습':
            c.label = 'green'
        elif c.label == '휴가':
            c.label = 'red'
    return render(request, './home/Fullcalendar.html', {'cal':cal})
