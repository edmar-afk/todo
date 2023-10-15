from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('<int:task_id>/deletetask/', views.deletetask, name='deletetask'),
    
]