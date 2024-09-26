from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Submission
def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'index.html', {'time': current_time})

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        submission = Submission(name=name, email=email)
        submission.save()
        return HttpResponse(f"Saved: Name - {name}, Email - {email}")
    return HttpResponse("Invalid request.")

def submissions(request):
    all_submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': all_submissions})
