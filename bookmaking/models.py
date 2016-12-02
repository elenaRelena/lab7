from django.db import models
from django import forms
from django.contrib.auth.models import User
import pymysql
from django.contrib.auth import authenticate
pymysql.install_as_MySQLdb()

class User1(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    stake = models.FloatField()
    contacts = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=50)
    
class Horse(models.Model):
    horse_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    ratio = models.FloatField()

class RegModel(forms.Form):
    username1 = forms.CharField(label='Username', min_length=5)
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', min_length=8, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', min_length=1)
    surname = forms.CharField(label='Surname', min_length=1)
    name = forms.CharField(label='Name', min_length=1)
    
    def clean (self):
        value = super(RegModel, self).clean()
        password = value.get('password')
        password2 = value.get('password2')
        if password!=password2:
            raise forms.ValidationError('Пароли должны совпадать')
        users = User.objects.filter(username=value.get('username1'))
        if len(users)>0:
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        
class LoginModel(forms.Form):
    username1 = forms.CharField(label='Username', min_length=5)
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput)
      
    def clean(self):
       cleaned_data=super(LoginModel, self).clean()
       if not self.errors:
           user = authenticate(username = cleaned_data['username1'], password = cleaned_data['password'])
           if user is None:
               raise forms.ValidationError('Неверный логин или пароль')
           self.user=user
       return cleaned_data
    def get_user(self):
        return self.user or None