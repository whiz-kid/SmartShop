# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from .forms import *
from django.shortcuts import render,redirect
from django.http import HttpResponseNotModified
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import *


class IndexView(generic.ListView):

    template_name = 'purchase/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


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
            return redirect('purchase:index')
        return render(request,self.template_name,{'form':form})

class UserLogoutView(generic.View):
    def get(self,request):
        logout(request)
        return redirect('purchase:index')


class UserProfileView(generic.View):

    template_name = 'purchase/userprofile.html'

    def get(self,request):
        user = User.objects.get(username=request.user.username)
        details = user.userdetails_set.all()
        return render(request,'purchase/userprofile.html',{'details':details})


class UserSettingView(generic.TemplateView):

    template_name = 'purchase/usersetting.html'


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
                return redirect('purchase:index')

        
        return render(request,self.template_name,{'form':form})


class ItemView(generic.ListView):

    template_name = 'purchase/item.html'
    context_object_name = 'category'

    def get_queryset(self):
        x1 = Category.objects.get(id=1)
        x3 = Category.objects.get(id=3)
        x8 = Category.objects.get(id=8)
        x={'x1':x1,'x3':x3,'x8':x8}
        return x

class DetailView(generic.DetailView):
    model = Item
    context_object_name = "item"
    template_name = 'purchase/details.html'

class CartDetailsView(generic.TemplateView):
    template_name = 'purchase/cartdetails.html'


class AddToCart(generic.View):

    template_name = 'purchase/item.html'

    def get(self,request,**kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        name = User.objects.get(username=request.user.username)
        c = Cart(customer=name,product=item)
        c.save()
        return redirect('purchase:item')


class AddToFavorite(generic.View):

    template_name = 'purchase/item.html'

    def get(self,request,**kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        name = User.objects.get(username=request.user.username)
        f = Favorite(customer=name,product=item)
        f.save()
        return redirect('purchase:item') 


class AddToLike(generic.View):

    template_name = 'purchase/item.html'

    def get(self,request,**kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        name = User.objects.get(username=request.user.username)
        l = Like(customer=name,product=item)
        l.save()
        return redirect('purchase:item')  

class PlaceOrder(generic.View):

    def get(self,request):
        #item = Item.objects.get(id=self.kwargs['pk'])
        name = User.objects.get(username=request.user.username)
        cart = Cart.objects.filter(customer_id=request.user.id)

        for c in cart:
            item = Cart.objects.get(id=c.id)
            o = Order(customer=name,product=item)
            o.save()

        return redirect('purchase:orderdetails')

class DeleteItem(generic.View):
    
    def get(self,request,**kwargs):
        Cart.objects.get(customer_id=request.user.id,product_id=self.kwargs['pk']).delete()
        return redirect('purchase:cartdetails')

class EmptyCart(generic.View):

    def get(self,request):
        items = Cart.objects.filter(customer_id=request.user.id)
        for item in items:
            Cart.objects.get(id=item.id).delete()

        return redirect('purchase:item')

class OrderDetails(generic.View):

    template_name = 'purchase/order.html'
    form_class = UserDetailsForm

    def get(self,request):
        cart = Order.objects.filter(customer_id=request.user.id)
        form = self.form_class
        return render(request,self.template_name,{'form':form,'cart':cart})
