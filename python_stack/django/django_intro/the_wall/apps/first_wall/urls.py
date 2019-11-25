from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.wall),
    path('logout', views.logout),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('delete_message/<number>', views.delete_message),
    path('delete_comment/<number>', views.delete_comment)
]