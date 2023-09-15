"""
URL configuration for finalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from studentinfo import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='studentinfo/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='studentinfo/logout.html'), name='logout'),
    path('studentinfo/', views.getStudentInfo, name='studentinfo'),
    path('courseinfo/', views.getCourseInfo, name='courseinfo' ),
    path('enrollment/', views.enrollment, name='enrollment'),
    path ('enrollment_page/<int:studentid>/', views.enrollment_page, name='enrollment_page'),

]
