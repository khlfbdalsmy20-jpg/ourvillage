from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('village.urls')), # ربط روابط تطبيق القرية بالسيرفر الرئيسي
]