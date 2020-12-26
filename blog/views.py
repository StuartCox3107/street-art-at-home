from django.shortcuts import render
from .models import Blogentry

# Create your views here.

def blog(request):
    """a view to show all blog entries"""

    blogentries = Blogentry.objects.all()

    context = {
        'blogentries': blogentries,
    }

    return render(request, 'blog/blog.html', context)