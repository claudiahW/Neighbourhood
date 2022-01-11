from django.contrib import admin
from django.urls import path,include
from neighs import views
 

urlpatterns = [
    path('',views.index, name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile,name='profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('create_hood/',views.create_hood,name = 'create_hood'),
    path('hoods/',views.hoods,name = 'hoods'),
    path('hood/<str:name>',views.single_hood,name='single_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path("create_business", views.create_business, name="create_business"),
    path("businesses/", views.businesses, name="businesses"),
    path('post/create_post', views.create_post, name='create_post'),
    path('post/', views.posts, name = 'post'),
    path('search/',views.search, name='search'),

   
]
