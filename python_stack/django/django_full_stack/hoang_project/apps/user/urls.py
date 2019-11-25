from django.urls import path
from . import views
                    
urlpatterns = [
    path('<int:number>', views.user_infor),
    path('<number>/friends', views.friend),
    path('checkfriend', views.checkfriend),
    path('post_post', views.post_post),
    path('remove_post', views.remove_post),
    path('<number>/edit',views.edit),
    path('editsubmit', views.editsubmit),
    path('add_friend', views.add_friend),
    path('delete_friend', views.delete_friend),
    # path('add_follow', views.add_follow),
    # path('delete_follow', views.delete_follow)
]