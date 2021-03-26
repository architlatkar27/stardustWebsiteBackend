from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'other/home.html', context)

    