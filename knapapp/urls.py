from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cal/', views.calculate, name='cal')
]
