from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.quote),
    path('logout', views.logout),
    path('post_quote', views.post_quote),
    path('users/<number>', views.user_infor),
    path('add_favorite', views.add_favorite),
    path('remove_favorite', views.remove_favorite),
    path('remove_quote', views.remove_quote),
    path('<number>',views.edit),
    path('<number>/edit', views.editsubmit)
]