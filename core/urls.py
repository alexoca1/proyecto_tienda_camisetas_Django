"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,  register, logout_view, lista_productos, my_usuario


urlpatterns = [
    path('', home, name='home'),    
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('productos/', lista_productos, name='lista_productos'),
    path('my_usuario/', my_usuario, name='my_usuario'),   # Cambiamos el nombre de la URL y de la vista
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
 
]

  
   
