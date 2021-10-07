from django.urls import path
from .import views


app_name= 'App_Blog'

urlpatterns = [
    path( '' , views.BlogList , name='BlogList'),
    path('write/' , views.CreateBlog.as_view() , name='CreateBlog'),
    path('details/<slug:slug>', views.blog_details , name="BlogDetails"),
    path('like/<pk>/', views.like , name="Like"),
    path('unlike/<pk>/', views.unlike , name="UnLike"),
]