from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .basket import Basket
from .forms import BasketAddClotheForm, OrderForm
from firstapp.models import Clothe, Order, Pos_Order

# Create your views here.
@login_required
def basket_detail(request):
    basket = Basket(request)
    return render(
        request,
        'basket/detail.html',
        context={
            'basket': basket
        }
    )

@login_required
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothe, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

@login_required
def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@login_required
@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Clothe, pk=product_id)
    form = BasketAddClotheForm(request.POST)
    if form.is_valid():
        basket.add(
            product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')

@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('clothes_list')
    
    form = OrderForm(request.POST)

    if form.is_valid():
        order = Order.objects.create(
            buyer_lastname = form.cleaned_data['buyer_lastname'],
            buyer_firstname = form.cleaned_data['buyer_firstname'],
            buyer_middlename = form.cleaned_data['buyer_middlename'],
            comment = form.cleaned_data['comment'],
            delivery_address = form.cleaned_data['delivery_address'],
            delivery_type = form.cleaned_data['delivery_type'],
        )
        for item in basket:
            pos_order = Pos_Order.objects.create(
                clothes=item['product'],
                count=item['count'],
                order=order,
            )
        basket.clear()
    return redirect('basket_detail')

@login_required
def open_order(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'order/order_form.html', context=context)