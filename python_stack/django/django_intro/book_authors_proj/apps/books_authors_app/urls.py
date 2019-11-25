from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    # path('bla', views.farming),
    # path('blabla', views.reset),
    path('add_books',views.add_books),
    path('books/<str:num>', views.bookinfor),
    path('update_book',views.updatebook),
    path('authors', views.add_author),
    path('authors/<str:num>', views.authorinfor),
    path('update_author',views.updateauthor)
]