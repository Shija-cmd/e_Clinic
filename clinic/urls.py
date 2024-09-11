
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from class_based_auth_views.views import LogoutView
from .views import download_excel
from .views import download_page

#Path to the urls
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout', LogoutView.as_view(template_name='clinic/login.html'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
    path('download/excel/', download_excel, name='download-excel'),
    path('download/', download_page, name='download'),
    
]
