from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag 
    Args: 
        item_id: Finds the correct chosen item
    Returns:
        changes the quantity of the item in the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)