from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('clothes/', ClotheListView.as_view(), name='clothes_list'),
    path('clothes/<int:pk>/', ClotheDetailView.as_view(), name='clothes_detail'),
    path('clothes/create/', ClotheCreateView.as_view(), name='clothes_create'),
    path('clothes/update/<int:pk>/', ClotheUpdateView.as_view(), name='clothes_update'),
    path('clothes/delete/<int:pk>/', ClotheDeleteView.as_view(), name='clothes_delete'),

    path('login/', login_user, name='login_page'),
    path('registration/', registration_user, name='registration_page'),
    path('logout/', logout_user, name='logout_page'),
]