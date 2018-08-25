from .models import *
from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
class Product_form(forms.ModelForm):
    class Meta():
        model=Product
        fields='__all__'

class Checkout_form(forms.ModelForm):
    class Meta():
        model=Checkout
        fields='__all__'


class Cart_form(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['quantity']

class Cart2_form(forms.ModelForm):
    class Meta:
        model=Cart2
        fields='__all__'


class user_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter username"}),required=True,max_length=20)
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}), required=True, max_length=20)  # check the validity of email
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter first name"}),required=True,max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter last name"}),required=True,max_length=20)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter the password"}),required=True,max_length=20)  #check the password nd show *****
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter the confirm password"}),required=True,max_length=20)

    class Meta():
        model=User
        fields=["username","email","first_name","last_name","password"]

    def clean_username(self):
        user=self.cleaned_data["username"]
        try:
            match=User.objects.get(username=user)
        except:
            return self.cleaned_data["username"]
        raise forms.ValidationError("user name already exists")


    def cleaned_email(self):
        email=self.cleaned_data["email"]
        try:
            ma=validate_email(email)
        except:
            raise forms.ValidationError("invalid email")
        return email

    def clean_confirm_password(self):
        p=self.cleaned_data["password"]
        cp=self.cleaned_data["confirm_password"]
        if(p!=cp):
            raise forms.ValidationError("both passwords are not matched")
        else:
            if(len(p)<8):
                raise forms.ValidationError("password must be atleast 8 characters")
            if(p.isnumeric()):
                raise forms.ValidationError("password must contains alleast a character")


