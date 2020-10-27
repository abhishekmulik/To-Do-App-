from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('update_task/<str:pk>/',views.update_task,name='update_task'),
        #str:pk bcz id can be both numbers and strings
    path('delete/<str:pk>/',views.deleteTask,name='delete'), 
]