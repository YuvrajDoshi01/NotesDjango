from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Notesview.as_view(), name='Notesview'),
    path('notes/<int:pk>',views.Notesdetail.as_view(),name ='Notesdetail'),
    path('create',views.Notescreate.as_view(),name= 'Notescreate'), 
    path('updatenotes/<int:pk>', views.Notesupdate.as_view(),name= 'Notesupdate'),
    path('deletenotes/<int:pk>', views.Notesdelete.as_view(),name= 'Notesdelete'),
    path('logout',LogoutView.as_view(next_page='login'),name = 'logout'),
    path('login',views.UserLogin.as_view(),name = 'login'),
    path('register',views.RegisterUser.as_view(),name = 'register'),
]
