from django.urls import path
from . import views
urlpatterns = [
    path('',views.LOGIN_PAGE,name='login'),

    path('dashboard/',views.DASHBORD,name='dashboard'),
    path('profile/',views.PROFILE,name='profile'),
    path('about/',views.ABOUT,name='about'),
    path('logout/',views.LOGOUT,name='logout'),

]