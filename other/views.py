from django.shortcuts import render
from Members.models import Faculty
# Create your views here.
def home_view(request):
    context = {}
    faculty = Faculty.objects.all().order_by('rank')
    context["faculty"] = faculty
    return render(request, 'other/index.html', context)

def contact_view(request):
    context = {}
    return render(request, 'other/contact.html', context)

def ss_view(request):
    context = {}
    return render(request, 'other/subsystems.html', context)