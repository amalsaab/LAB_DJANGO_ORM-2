from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('blog/add/', views.add_page, name="add_page"),
    path('blog/read/<blog_id>', views.read_blog, name="read_blog"),
    path('blog/update/<blog_id>', views.update_blog, name="update_blog"),
    path('blog/delete/<blog_id>', views.delete_blog, name="delete_blog"),
    path('blog/search/', views.search_blog, name="search_blog"),
    path('blog/read/not/found', views.notfoundpafe, name="notfoundpafe"),

]