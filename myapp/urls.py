from django.urls import path
from . views import index,about,blog,contact,login,pricing,register,logout

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('pricing/',pricing,name='pricing'),
    path('logout/',logout,name='logout'),
]
