"""playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import appointments_by_user, generate_users, delete_users, get_users, get_usernames, get_ethnicities, delete_data, generate_appointment_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_users', generate_users, name="generate_users"),
    path('delete_users', delete_users, name="delete_users"),
    path('delete_objects', delete_data, name="delete_users"),
    path('get_users/<int:limit>', get_users, name="get_users"),
    path('get_usernames/<int:limit>', get_usernames, name="get_usernames"),
    path('get_ethnicities/<int:limit>', get_ethnicities, name="get_ethnicities"),
    path('create_data/', generate_appointment_data, name="generate_data"),
    path('appointments_by_user', appointments_by_user, name="appointments_by_user"),
    path('silk/', include('silk.urls', namespace='silk'))    
]
