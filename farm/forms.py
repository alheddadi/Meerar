from django.forms import ModelForm

from farm.models import User,Product,Reports
from django.contrib.auth.models import Group
from django import forms

class RegisterForm(ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name','Number','email','password','gobolka','magaalada','user_pic','group']

        widgets = {
            'name':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),
            'Number':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),
            'email':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),

            
          }

class newFORM(ModelForm):
    class Meta:
        model = Product
        fields = ['name','amount','unit','product_pic',]

        widgets = {
            'name':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),
            'amount':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),
            'unit':forms.TextInput(
            attrs ={'id':'desc','style': 'border-color:green; border-radius: 10px;','size':'30'}),

            
          }


class reportsForm(ModelForm):
    class Meta:
        model = Reports
        fields = ['Product','amount','price']
        
            