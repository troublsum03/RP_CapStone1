from django.shortcuts import render, redirect

from greenery.models import Greenery
from .models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
    greenery_id = request.POST.get('greenery_id')
    if greenery_id is not None:
        try:
            greenery_obj = Greenery.objects.get(id=greenery_id)
        except Greenery.DoesNotExist:
            print("Show message to user, we ain't got it?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if greenery_obj in cart_obj.greenery.all():
            cart_obj.greenery.remove(greenery_obj)
        else:
            # cart_obj.greenery.add(greenery_id)
            cart_obj.greenery.add(greenery_obj)
        request.session['cart_items'] = cart_obj.greenery.count()
        # return redirect(greenery_obj.get_absolute_url())
    return redirect("cart:home")
