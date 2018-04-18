from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'<int:pk>/base/', views.BaseView.as_view(), name='base'),
    url(r'<int:pk>/home/', views.HomeView.as_view(), name='home'),
]