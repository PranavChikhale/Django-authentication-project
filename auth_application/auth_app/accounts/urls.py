from django.urls import path
from . import views
from .views import user_list
urlpatterns = [
    path('',views.LOGIN_PAGE,name='login'),
    path('user/',user_list,name='user_list'),
    path('register/',views.register,name='register'),
    path('api/register/',views.register_api,name='register_api'),

    path('dashboard/',views.DASHBORD,name='dashboard'),
    path('profile/',views.PROFILE,name='profile'),
    path('about/',views.ABOUT,name='about'),
    path('logout/',views.LOGOUT,name='logout'),


]