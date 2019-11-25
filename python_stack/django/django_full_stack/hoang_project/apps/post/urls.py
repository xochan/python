from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.post),
    path('logout', views.logout),
    path('post_post', views.post_post),
    path('add_favorite', views.add_favorite),
    path('<number>/remove_favorite', views.remove_favorite),
    path('remove_post', views.remove_post),
    path('<number>/edit', views.editsubmit),
    path('<number>/favorite', views.user_favorite)
]