from django.shortcuts import render
from .models import ResearchPaper
# Create your views here.
def research_view(request):
    context = {}
    all_papers = ResearchPaper.objects.all().order_by("-year")
    
    # for paper in all_papers:
    #     try:
    #         context[paper.year].append(paper)
    #     except:
    #         context[paper.year] = []
    #         context[paper.year].append(paper)
    context['papers'] = all_papers
            
    return render(request,'Research/research.html',context)