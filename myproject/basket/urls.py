from django.urls import path
from .views import basket_detail, basket_remove, basket_add, basket_buy, basket_clear, open_order

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('clear/', basket_clear, name='basket_clear'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('buy/', basket_buy, name='basket_buy'),
    path('create_order/', open_order, name='order_open'),
]
