from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('addsuccess', views.addsuccess),
    path('logout', views.logout),
    path('login', views.login)
]