from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    # path('bla', views.farming),
    # path('blabla', views.reset),
]