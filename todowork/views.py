from django.shortcuts import render

from django.http import HttpResponse ,HttpResponseRedirect
from .models import TodoItem

def homePageView(request):
	all_todo_items = TodoItem.objects.all()

	return render(request,'home.html', {'all_todo_items':all_todo_items})


def addTodo(request):
	new_item=TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
	item_to_delete=TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/')