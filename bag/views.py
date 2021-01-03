from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag 
    Args:
        request: HTTP request 
        item_id: Finds the correct chosen item
    Returns:
        Changes the quantity of the item in the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added more {product.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """adjust the quantity of the specified product to the specified amount
    Args: 
        request: HTTP request 
        item_id: Finds the correct chosen item
    Returns:
        If number is adjusted to zero the item is removed from the bag when the update button is clicked, otherwise number in cart is adjusted
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def handler404(request, exception):
    """ Handler for 404 errors
    Args:
        request: HTTP request object
        exception: exception raised
    Returns:
        Rendered 404 html
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """ Handler for 500 errors
    Args:
        request: HTTP request object
    Returns:
        Rendered 500 html
    """
    return render(request, '500.html', status=500)
