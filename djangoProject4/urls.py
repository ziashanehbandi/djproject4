"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #AUTH

    path('signup/',SignUpUser,name='SignUpUser'),
    path('logout/',LogoutUser,name='LogoutUser'),
    path('login/',LoginUser,name='LoginUser'),




    #todoo
    path('todo/<int:todo_pk>',each_todo,name='each_todo'),
    path('todo/<int:todo_pk>/complete',completeTodo,name='completeTodo'),
    path('todo/<int:todo_pk>/delete',deleteTodo,name='deleteTodo'),
    path('create/',CreateTodo,name='CreateTodo'),
    path('current/',current,name='current'),
    path('completed/',completedTodo,name='completedTodo'),
    path('',home,name='home'),
]
