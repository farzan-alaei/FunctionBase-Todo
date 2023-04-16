from django.urls import path
from . import views
app_name = 'todo'


urlpatterns = [
    path('', views.list_view, name='task-list'),
    path('update/<int:pk>/', views.update_task, name='update-task'),
    path('complete/<int:pk>/', views.complete_task, name='complete-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]
