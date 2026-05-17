from django.shortcuts import render
from .models import Contact
from django.http import FileResponse

def index(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
    return render(request, 'index.html')


def download_cv(request):
    return FileResponse(open('media/resume.pdf', 'rb'), as_attachment=True)