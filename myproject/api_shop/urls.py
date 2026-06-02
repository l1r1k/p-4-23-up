from rest_framework import routers
from .views import *

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register('categories', CategoryViewSets, basename='categories')
router.register('collections', CollectionViewSets, basename='collections')
router.register('clothes', ClotheViewSets, basename='clothes')
router.register('orders', OrderViewSets, basename='orders')
router.register('pos-orders', PosOrderViewSets, basename='pos-orders')

urlpatterns += router.urls