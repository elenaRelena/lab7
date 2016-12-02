from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import User1, RegModel, LoginModel
from django.views import View
from pip._vendor import requests
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
 

#class user_view(View):
@login_required(login_url='/login')
def user_view(request):
#def get(request):
    users = User1.objects.all()
    return render (request, 'bookmaking/users.html', {'users': users})
    
def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/login') 
def main_page(request):
    return render (request, 'bookmaking/main_page.html', {})

class Registration(View):
    def get(self, request):
        form = RegModel()
        return render(request, 'bookmaking/registration2.html',{'errors':'', 'form': form.as_p()})
   
    def post (self, request):
        form = RegModel(request.POST)  
        if not form.is_valid():
            return render(request, 'bookmaking/registration2.html', {'errors': '', 'form': form.as_p()}) 
        us = User(username=form.cleaned_data['username1'], email=form.cleaned_data['email'], last_name=form.cleaned_data['surname'], first_name=form.cleaned_data['name'])
        us.set_password(form.cleaned_data['password'])
        us.save(form.cleaned_data['username1'])
        user = authenticate(username=form.cleaned_data['username1'], password=form.cleaned_data['password'])
        login(request, user)    
        return redirect('/')   
    
# class Registration(View):
#     def get(self, request):
#         return render(request, 'bookmaking/registration.html',{'errors':'', 'username':'', 'email':'', 'surname':'', 'name':''})
#   
#     def post (self, request):       
#         errors = []
#         if request.method == 'POST':
#             username1 = request.POST['username']
#             password = request.POST['password']
#             password2 = request.POST['password2']
#             email = request.POST['email']
#             surname = request.POST['surname']
#             name = request.POST['name']
#             if not username1:
#                 errors.append('Введите логин')
#             if not surname:
#                 errors.append('Введите фамилию')
#             if len(username1)<5:
#                 errors.append('Слишком короткий логин')
#               
#             if len(password)<8:
#                 errors.append('Слишком короткий пароль')  
#             if password!=password2:
#                 errors.append('Пароли должны совпадать')
#               
#             if len(errors)==0:
#                 users=User.objects.filter(username=username1)
#                 if len(users)>0:
#                     errors.append('Пользователь с таким именем уже существует')                 
#                 else:
#                     us = User(username=username1, email=email, last_name=surname, first_name=name)   
#                     us.set_password(password)
#                     us.save()
#             if len(errors)>0:
#                 return render(request, 'bookmaking/registration.html', {'errors':mark_safe('<br>'.join(errors)), 'username1':username1, 'email':email, 'surname':surname, 'name':name})
#         return redirect('/')   
        
         
class Login (View):
     def get(self,request):
         return render(request, 'bookmaking/login.html', {'errors':'', 'username':''})
 
     def post(self, request):
         username1 = request.POST['username']
         password = request.POST['password']
         errors = []
 
         user = authenticate(username=username1, password=password)
 
         if user is not None:
             login(request, user)
             return redirect('/')
         errors.append('Логин или пароль неверны')
         return render(request, 'bookmaking/login.html', {'errors': mark_safe('<br>'.join(errors)), 'username': username1})
     
def log_in(request):    
    if request.method == 'POST':
        form = LoginModel(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return redirect('/')           
    else: 
       form=LoginModel()
    return render(request, 'bookmaking/login2.html', {'form': form.as_p()})

        
