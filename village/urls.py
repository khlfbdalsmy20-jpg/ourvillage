from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-service-outside/', views.add_service_from_outside, name='add_service_outside'),
    
    # روابط إخفاء أو إتمام الخدمات
    path('complete-blood/<int:pk>/', views.complete_blood, name='complete_blood'),
    path('complete-medical/<int:pk>/', views.complete_medical, name='complete_medical'),
    path('complete-transport/<int:pk>/', views.complete_transport, name='complete_transport'),
    path('complete-craft/<int:pk>/', views.complete_craft, name='complete_craft'),
]