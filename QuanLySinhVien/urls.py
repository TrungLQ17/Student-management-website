"""
URL configuration for QuanLySinhVien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sinhvien import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sinhvien_list/', views.sinhvien_list, name='sinhvien_list'),
    path('sinhvien_totnghiep/', views.sinhvien_totnghiep, name='sinhvien_totnghiep'),
    path('sinhvien_khong_totnghiep/', views.sinhvien_khong_totnghiep, name='sinhvien_khong_totnghiep'),
    path('sinhvien_max_dtb/', views.sinhvien_max_dtb, name='sinhvien_max_dtb'),
    path('sinhvien_min_dtb/', views.sinhvien_min_dtb, name='sinhvien_min_dtb'),
    path('tim_kiem/', views.tim_kiem_sv, name='tim_kiem_sv'),

]
