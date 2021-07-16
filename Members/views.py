from django.shortcuts import render
from Members.models import Student, Technical, Rocketry, NonTechnical

# Create your views here.

def team_view(request):
    context = {}
    tech_members        = Technical.objects.filter(member__is_active=True).order_by("subsystem", "rank")
    roc_members         = Rocketry.objects.filter(member__is_active=True).order_by("subsystem", "rank")
    non_tech_members    = NonTechnical.objects.filter(member__is_active=True).order_by("team","rank")
    founders            = Student.objects.filter(status="F").order_by("rank")
    core                = Student.objects.filter(status="C").order_by("rank")
    context["founders"] = founders
    context["core"]     = core
    context["tech"]     = tech_members
    context["roc"]      = roc_members
    context["nontech"]  = non_tech_members
    # context["spm"] = Student.objects.get(core_postion="SPM")
    # context["pm"] = Student.objects.filter(core_position="PM")
    # context["mm"] = Student.objects.filter(core_position="MM")
    # context["md"] = Student.objects.filter(core_position="MD")
    # context["tm"] = Student.objects.get(core_position="TM")
    # print(context["tech"])
    return render(request, 'Members/team.html', context)

# def non_tech_team(request):
#     pass

