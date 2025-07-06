from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('api/user/', views.user_info, name='user_info'),
    path('api/tasks/', views.task_list_api, name='task_list_api'),
]