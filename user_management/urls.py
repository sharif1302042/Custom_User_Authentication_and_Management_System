from django.urls import path
from user_management import views

urlpatterns = [
    path('create/', views.UserCreate.as_view(), name="user/create/"),
    path('thank_you/', views.ThankYou.as_view(), name="user/thanks/"),
    path('login/', views.Login.as_view(), name="user/login/"),
    path('dashboard/', views.Dashboard.as_view(), name="user/dashboard/"),
]
