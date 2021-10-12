from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name='home'),
    path('new_url/<str:pk>/', views.newUrl, name='short_url'),
    path('u/<str:slugs>/', views.urlRedirect, name='redirect'),
    
]