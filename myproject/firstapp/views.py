from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Collection, Clothe
from .forms import ClotheForm, LoginForm, RegistrationForm
from basket.forms import BasketAddClotheForm

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class ClotheListView(ListView):
    model = Clothe
    template_name = 'clothe/clothes_list.html'
    context_object_name = 'clothes'

class ClotheDetailView(DetailView):
    model = Clothe
    template_name = 'clothe/clothes_detail.html'
    context_object_name = 'clothes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddClotheForm()
        return context

class ClotheCreateView(UserPassesTestMixin,CreateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'clothe/clothes_form.html'
    success_url = reverse_lazy('clothes_list')
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

class ClotheUpdateView(UserPassesTestMixin,UpdateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'clothe/clothes_form.html'
    success_url = reverse_lazy('clothes_list')
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

class ClotheDeleteView(UserPassesTestMixin,DeleteView):
    model = Clothe
    template_name = 'clothe/clothes_delete.html'
    success_url = reverse_lazy('clothes_list')
    context_object_name = 'clothes'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

from django.contrib.auth import login, logout

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')