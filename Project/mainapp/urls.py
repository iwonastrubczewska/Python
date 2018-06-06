from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    # path('base/', views.BaseView.as_view(), name='base'),
    path('offer/<int:pk>', views.OfferView.as_view(), name='offer'),
    url(r'^offer/new/$', views.NewOffer, name='newoffer'),
    url(r'^user/signin$', views.SignIn, name='signin'),
    url(r'^user/login$', views.LogIn, name='login'),
    url(r'^user/contact$', views.Contact, name='contact'),
]
