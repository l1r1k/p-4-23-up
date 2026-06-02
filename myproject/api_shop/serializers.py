from rest_framework import serializers
from firstapp.models import Category, Collection, Clothe, Order, Pos_Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description' 
        ]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'name',
            'description' 
        ]

class ClotheSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=8, decimal_places=2)

    class Meta:
        model = Clothe
        fields = [
            'pk',
            'name',
            'description',
            'price',
            'size',
            'photo',
            'is_exists',
            'category',
            'collections'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_lastname',
            'buyer_firstname',
            'buyer_middlename',
            'comment',
            'delivery_address',
            'delivery_type',
            'datetime_create',
            'datetime_finish',
            'clothes',
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_Order
        fields = '__all__'