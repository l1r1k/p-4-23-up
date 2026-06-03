from rest_framework import viewsets
from .serializers import CategorySerializer, CollectionSerializer, ClotheSerializer, OrderSerializer, PosOrderSerializer
from firstapp.models import Category, Collection, Clothe, Order, Pos_Order
from .permissions import CustomPermissions, PaginationPage, OnlyPostPermission
from rest_framework import mixins

from rest_framework.renderers import AdminRenderer


# Create your views here.
class CategoryViewSets(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset

class CollectionViewSets(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    renderer_classes = [AdminRenderer]

class ClotheViewSets(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Clothe.objects.all()
    serializer_class = ClotheSerializer
    permission_classes = [OnlyPostPermission]

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    renderer_classes = [AdminRenderer]

class PosOrderViewSets(viewsets.ModelViewSet):
    queryset = Pos_Order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    renderer_classes = [AdminRenderer]