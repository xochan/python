from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<str:num>', views.showinfor),
    path('new', views.createshow),
    path('create', views.create),
    path('shows/<str:num>/edit', views.edit),
    path('update', views.update),
    path('delete/<str:num>', views.delete)
    # path('bla', views.farming),
    # path('blabla', views.reset),
]