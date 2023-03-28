from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('read_all', views.taskList, name='task-list'),
	path('tasks/<int:id>', views.taskView, name='task-view'),
	path('create/', views.newTask, name='add-task'),
	path('update/<int:id>', views.editTask, name='edit-task'),
	path('delete/<int:id>', views.deleteTask, name='delete-task')
]