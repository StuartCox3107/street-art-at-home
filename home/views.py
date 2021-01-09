from django.shortcuts import render


def index(request):
    """ A view to return the index page
    Args:
        request: HTTP request
    Returns: The rendered index.html page """

    return render(request, 'home/index.html')
