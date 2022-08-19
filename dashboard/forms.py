from django import forms
from .models import Companies, Placements, Product, Order, Students


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'order_quantity']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = '__all__'


class PlacementForm(forms.ModelForm):

    class Meta:
        model = Placements
        fields = '__all__'


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = '__all__'