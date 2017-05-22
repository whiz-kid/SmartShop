# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from .forms import UserForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class IndexView(generic.TemplateView):

    template_name = 'purchase/index.html'

class UserView(generic.TemplateView):

    template_name = 'purchase/user.html'

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
            #user.set_password(password)
            user.save()

            user = authenticate(username = username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('purchase:user')

        
        return render(request,self.template_name,{'form':form})


