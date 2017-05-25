from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'purchase'

urlpatterns = [
    url(r'^index/$',views.IndexView.as_view(),name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    #url(r'^login/$',login,{'template_name':'purchase/login.html'},name='login'),
    url(r'^login/$',views.UserLoginView.as_view(),name='login'),
    #url(r'^logout/$',logout,{'next_page':'/index'},name='logout'),
    url(r'^logout/$',views.UserLogoutView.as_view(),name='logout'),
    url(r'^user/(?P<pk>[0-9]+)/$',login_required(views.UserView.as_view(),login_url='purchase:login'),name='user'),
    url(r'^item/$',views.ItemView.as_view(),name='item'),
    url(r'^item/(?P<pk>[0-9]+)/details/$',views.DetailView.as_view(),name='details'),
    url(r'^item/(?P<pk>[0-9]+)/add/$',views.AddToCart.as_view(),name='add'),
]

