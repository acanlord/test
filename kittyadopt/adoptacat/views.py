from django.shortcuts import render

def adoption_homepage(request):
        context = {
            'adoptions_needed': 5,
        }
        return render(request, 'adoption_homepage.html', context)

# Create your views here.
