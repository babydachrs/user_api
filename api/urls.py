from django.urls import path
from . import views


urlpatterns = [
    #path('', views.apiOverview, firstname='apiOverview'),
    path('user-list/', views.ShowAll, name='user-list'),
    path('user-detail/<int:pk>/', views.ViewUser, name='user-detail'),
    path('user-create/', views.CreateUser, name='user-create'),
    path('user-update/<int:pk>/', views.UpdateUser, name='user-update'),
    path('user-delete/<int:pk>/', views.DeleteUser, name='user-delete'),

]