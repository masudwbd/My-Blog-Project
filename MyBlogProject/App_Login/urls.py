from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/' , views.sign_up , name="Signup"),
    path('login/', views.login_page , name="Login"),
    path('logout/', views.logout_user , name="Logout"),
    path('profile/', views.profile , name="Profile"),
    path('userchange/', views.user_change , name="UserChange"),
    path('password/', views.pass_change, name="PassChange" ),
    path('add-picture' , views.add_pro_pic , name='AddProPic'),
    path('change-picture' , views.change_pro_pic , name='ChangeProPic'),

]
