from django.shortcuts import render
from .models import Citiesentry

# Create your views here.

def cities(request):
    """a view to show all blog entries"""

    cities = Citiesentry.objects.all()

    context = {
        'cities': cities,
    }

    return render(request, 'cities/cities.html', context)