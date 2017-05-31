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
   # url(r'^user/(?P<pk>[0-9]+)/$',login_required(views.UserView.as_view(),login_url='purchase:login'),name='user'),
    url(r'^item/$',views.ItemView.as_view(),name='item'),
    url(r'^item/(?P<pk>[0-9]+)/details/$',views.DetailView.as_view(),name='details'),
    url(r'^item/(?P<pk>[0-9]+)/add/$',views.AddToCart.as_view(),name='add'),
    url(r'^item/(?P<pk>[0-9]+)/like/$',views.AddToLike.as_view(),name='like'),
    url(r'^item/(?P<pk>[0-9]+)/favorite/$',views.AddToFavorite.as_view(),name='favorite'),
    url(r'^user/cart/$',views.CartDetailsView.as_view(),name='cartdetails'),
    url(r'^user/cart/order/$',views.PlaceOrder.as_view(),name='order'),
    url(r'^user/cart/(?P<pk>[0-9]+)/delete/$',views.DeleteItem.as_view(),name='deleteitem'),
    url(r'^user/cart/empty/$',views.EmptyCart.as_view(),name='emptycart'),
    url(r'^user/cart/order/orderdetails$',views.OrderDetails.as_view(),name='orderdetails'),
    url(r'^user/profile/$',views.UserProfileView.as_view(),name='userprofile'),
    url(r'^user/setting/$',views.UserSettingView.as_view(),name='usersetting'),
]

