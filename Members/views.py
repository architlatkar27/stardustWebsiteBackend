from django.shortcuts import render
from Members.models import Student, Technical, NonTechnical

# Create your views here.

def team_view(request):
    context = {}
    tech_members = Technical.objects.filter(member__is_active=True).order_by("subsystem")
    non_tech_members = NonTechnical.objects.filter(member__is_active=True).order_by("team")
    context["tech"] = tech_members
    context["nontech"] = non_tech_members
    # context["spm"] = Student.objects.get(core_postion="SPM")
    # context["pm"] = Student.objects.filter(core_position="PM")
    # context["mm"] = Student.objects.filter(core_position="MM")
    # context["md"] = Student.objects.filter(core_position="MD")
    # context["tm"] = Student.objects.get(core_position="TM")
    return render(request, 'Members/members.html', context)

# def non_tech_team(request):
#     pass

