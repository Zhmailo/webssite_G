from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.order.forms import AddToCartForm, CreateOrderForm
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


@login_required
def cart_view(request):
    cart = get_cart_data(request.user)
    breadcrumbs = {'current': "Кошик"}
    return render(request, 'order/cart_view.html', {'cart': cart, 'breadcrumbs': breadcrumbs})


@login_required
def create_order_view(request):
    error = None
    user = request.user
    cart = get_cart_data(user)
    if not cart['cart']:
        return redirect('index')

    if request.method == 'POST':
        data = request.POST.copy()
        data.update(user=user, total=cart['total'])
        request.POST = data

        form = CreateOrderForm(request.POST)
        if form.is_valid():
            form.save()
            Cart.objects.filter(user=user).delete()
            return render(request, 'order/created.html')
        error = form.errors
    else:
        form = CreateOrderForm(data={
            'phone': user.phone if user.phone else '',
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
    return render(request, 'order/create.html', {'cart': cart, 'error': error, 'form': form})
