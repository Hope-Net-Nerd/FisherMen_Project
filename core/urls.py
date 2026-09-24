from django.urls import path
from . import views

urlpatterns=[
   path("", views.home, name="home"),
   path("blogs/", views.blogs, name="blogs"),
   path("about/", views.about, name="about"),
   path("books/", views.books, name="books"),
   path("post/",views.create_post, name="post"),
   path("media/<int:pk>/edit",views.edit_media,name="edit_media"),
   path("media/<int:pk>/delete", views.delete_media, name="delete_media"),
]