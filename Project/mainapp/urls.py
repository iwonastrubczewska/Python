from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('base/', views.BaseView.as_view(), name='base'),




]
