from django.urls import path
from coursemanager import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('', views.WelcomeView.as_view()),
    
]