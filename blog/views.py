from django.shortcuts import render
from .models import Blogentry

# Create your views here.

def blog(request):
    """a view to show all blog entries"""

    blog = Blogentry.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)