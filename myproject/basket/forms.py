from django import forms

from firstapp.models import Order

class BasketAddClotheForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, label='Количество', 
                               widget=forms.NumberInput(attrs={'class': 'num-input'}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_lastname',
            'buyer_firstname',
            'buyer_middlename',
            'comment',
            'delivery_address',
            'delivery_type'
        )