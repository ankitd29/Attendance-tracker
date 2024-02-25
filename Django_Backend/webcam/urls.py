from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='webcam-index'),
    path('video/', views.video, name='webcam-video'),
]