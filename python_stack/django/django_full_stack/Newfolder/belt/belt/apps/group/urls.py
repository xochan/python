from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.group),
    path('/logout', views.logout),
    path('/create', views.create),
    path('/delete', views.delete),
    path('/<idnumber>', views.infor),
    path('/<idnumber>/join_leave', views.join_leave),
    # path('/<idnumber>/join', views.join),
    # path('/<idnumber>/leave', views.leave)
]