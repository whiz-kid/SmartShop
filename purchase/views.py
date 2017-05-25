# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from .forms import UserForm,LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from .models import Item,Category,Cart


class IndexView(generic.TemplateView):

    template_name = 'purchase/index.html'

class UserView(generic.TemplateView):

    template_name = 'purchase/index.html'

class UserLoginView(generic.View):
    template_name = 'purchase/login.html'
    form_class = LoginForm
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('purchase:user',pk=request.user.pk)
        return render(request,self.template_name,{'form':form})

class UserLogoutView(generic.View):
    def get(self,request):
        logout(request)
        return redirect('purchase:index')

class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'purchase/register.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username,password=password)

            if user is not None:
                
                login(request,user)
                return redirect('purchase:user',pk=request.user.pk)

        
        return render(request,self.template_name,{'form':form})


class ItemView(generic.ListView):

    template_name = 'purchase/item.html'
    context_object_name = 'category'

    def get_queryset(self):
        x1 = Category.objects.get(id=1)
        x3 = Category.objects.get(id=3)
        x={'x1':x1,'x3':x3}
        return x

class DetailView(generic.DetailView):
    model = Item
    context_object_name = "item"
    template_name = 'purchase/details.html'

class AddToCart(generic.View):

    template_name = 'purchase/item.html'

    def get(self,request,**kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        name = User.objects.get(username=request.user.username)
        c = Cart(customer=name,product=item)
        c.save()
        return redirect('purchase:item')
