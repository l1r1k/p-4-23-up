from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Collection, Clothe, Order, Pos_Order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Clothe)
class ClotheAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name', 
        'description', 
        'price', 
        'size', 
        'photo', 
        'created_at', 
        'updated_at', 
        'is_exists', 
        'category',
        'show_collections'
    ]

    def show_collections(self, obj):
        collections = Collection.objects.filter(clothe=obj).all()
        return ', '.join([collection.name for collection in collections])
    show_collections.short_description = 'Коллекции'

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 250px;" />',
                obj.photo.path
            )
        else:
            return '-'
    photo_preview.short_description = 'Превью фото одежды'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_Order)
class OrderAdmin(admin.ModelAdmin):
    pass