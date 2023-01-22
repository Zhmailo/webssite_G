from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.order.forms import AddToCartForm
from apps.order.models import Cart


def get_cart_data(user):
    total = 0
    cart = Cart.objects.filter(user=user).select_related('product')
    for row in cart:
        total += row.quantity * row.product.price

    return {'total': total, 'cart': cart}


@login_required
def add_to_cart(request):
    data = request.GET.copy()
    data.update(user=request.user)
    request.GET = data

    form = AddToCartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        row = Cart.objects.filter(user=cd['user'], product=cd['product']).first()
        if row:
            Cart.objects.filter(id=row.id).update(quantity=row.quantity + cd['quantity'])
        else:
            form.save()

    return render(request, 'order/cart_view.html', {'cart': get_cart_data(request.user)})  #


@login_required  #
def cart_view(request):  #
    return render(request, 'order/cart_view.html', {'cart': get_cart_data(request.user)})  #
