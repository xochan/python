from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('message/<int:real>/<int:idnumber>/create', views.chat_create),
    path('message/<int:id>/', views.chat),
    path('message', views.message)
]