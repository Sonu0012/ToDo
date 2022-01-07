from django.contrib import admin
from django.urls import path
from .views import CustomLoginView, TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('', TaskList.as_view(), name= 'task' ),
    path('task/<int:pk>/',TaskDetail.as_view(), name='detail'),
    path('create',TaskCreate.as_view(),name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='delete'),
    
]
