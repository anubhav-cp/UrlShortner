from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home')
]