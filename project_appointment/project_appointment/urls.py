"""
URL configuration for project_appointment project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home.as_view(), name='home'),
    path('appoint/', views.Appoint.as_view(), name='appoint'),
    path('doctor/', views.Doctor, name='Doctor'),
    path('done/<int:id>', views.History, name='done'),
    path('d_signup/', views.Doc_Sign, name="d_signup"),
    path('login/', views.d_login, name='login'),
    path('u_signup/', views.user_Sign, name='u_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('u_logout/', views.user_logout, name='u_logout'),
    path('filter/',views.DateFilter,name='filter')
]
