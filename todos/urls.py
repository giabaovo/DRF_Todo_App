from django.urls import path
from todos.views import *

app_name = 'todos'

urlpatterns = [
    path('create/', CreateTodoAPIView.as_view(), name='create_todo'),
    path('list/', ListTodoAPIView.as_view(), name='list_todo'),
]
