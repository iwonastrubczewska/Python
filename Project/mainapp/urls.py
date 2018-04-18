from atm import path
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'<int:pk>/base/', views.BaseView.as_view(), name='base'),
    path(r'<int:pk>/home', views.HomeView.as_view(), name='home'),
]