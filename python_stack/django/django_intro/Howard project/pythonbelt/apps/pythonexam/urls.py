from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.groups),
    path('logout', views.logout),
    path('add_group', views.add),
    path('groups/<str:num>/smallgroup', views.small_group),
    path('join_group', views.join_group),
    path('leave_group', views.leave_group),
]