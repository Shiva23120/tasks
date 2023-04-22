from django.urls import path

from . import views

urlpatterns = [
    path('logout/',views.logoutUser,name="logout"),
    path('',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),

    path('tasks/',views.tasks,name="tasks"),
    path('tasks/task/<str:pk>/',views.task,name="task"),
    path('addtask/',views.addtask,name='addtask'),
    path('updatetask/<str:pk>/',views.updatetask,name="updatetask"),
    path('deletetask/<str:pk>/',views.deletetask,name="deletetask")

]
