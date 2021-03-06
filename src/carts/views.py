from django.shortcuts import render, redirect


from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

from addresses.forms import AddressForm
from addresses.models import Address

from billing.models import BillingProfile
from orders.models import Order
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


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.greenery.count() == 0:
        return redirect("cart:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
        request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(
                billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(
            billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(
                id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(
                id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()

    if request.method == "POST":
        "check the order to see if it done"
        is_done = order_obj.check_done()
        order_obj.mark_paid()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("cart:success")

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs,
    }
    return render(request, "carts/checkout.html", context)


def checkout_done_view(request):
    return render(request, "carts/checkout_done.html", {})



