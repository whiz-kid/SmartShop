from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name = 'purchase'

urlpatterns = [
    url(r'^index/$',views.IndexView.as_view(),name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^login/$',login,{'template_name':'purchase/login.html'},name='login'),
    url(r'^logout/$',logout,{'next_page':'/index'},name='logout'),
    url(r'^user/$',views.UserView.as_view(),name='user'),

]

