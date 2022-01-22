from django.contrib import admin
from django.urls import path
from .views import *
app_name = "empsys"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('add-employee/',AddEmployeeView.as_view(),name="addemp"),
    path('view-employee/<int:id>',EmployeeShowView.as_view(),name="viewemp"),
    path('delete-employee/<int:pk>/', EmployeeDeleteView.as_view(), name="delemp"),
    path('edit-employee/<int:pk>/', EmployeeEditView.as_view(), name="editemp"),
    path('search/',SearchView.as_view(),name="search"),
    path('register/',UserRegisterView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path("logout/",UserLogoutView.as_view(),name="logout"),
]
