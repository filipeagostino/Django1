from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('read_all/', views.itemsList, name='items-list'),
    path('item/<int:id>', views.itemView, name='item-view'),
	path('create/', views.newItem, name='add-item'),
	path('update/<int:id>', views.editItem, name='edit-item'),
	path('delete/<int:id>', views.deleteItem, name='delete-item')
]