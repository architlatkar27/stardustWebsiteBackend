from django.shortcuts import render
from Achievements.models import Achievement
# Create your views here.
def acheivements_view(request):
    context = {}
    context["achievements"] = Achievement.objects.all().order_by("-date")
    return render(request, 'Achievements/achievements.html',context)