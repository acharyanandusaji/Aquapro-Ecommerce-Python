from django.shortcuts import render, redirect, get_object_or_404
# from shop.models import *
from shop.models import products
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def cartDetails(request, tot=0, count=0, ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.Quan)
            count += i.Quan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {"ci": ct_items, "t": tot, "cn": count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)

    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_items = items.objects.get(prodt=prod, cart=ct)
        if ct_items.quan < ct_items.prodt.stock:
            ct_items.quan += 1
        ct_items.save()
    except items.DoesNotExist:
        ct_items = items.objects.create(prodt=prod, Quan=1, cart=ct)
        ct_items.save()
    return redirect('cartDetails')

    def min_cart(request):
        pass

    def cart_delete(request):
        pass
