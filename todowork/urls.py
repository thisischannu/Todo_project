from django.urls import path

from .views import homePageView, addTodo, deleteTodo

urlpatterns = [
	path('', homePageView, name='home'),
	path('addtodo/', addTodo, name='addtodo'),
	path('deletetodo/<int:todo_id>', deleteTodo, name='deletetodo'),
 
]