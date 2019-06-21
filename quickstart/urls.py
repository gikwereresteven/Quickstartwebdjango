
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('quickstart/', views.registration_list, name='registration_list'),
    path('quickstart<int:pk>/', views.registration_detail, name='registration_detail'),
    path('home/',views.homepage, name='homepage'),
]