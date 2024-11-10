from django.urls import path
from .views import *

urlpatterns = [
    path('user/register/', RegisterUser.as_view(), name='register'),
    path('user/login/', UserLogin.as_view(), name='login'),
    path('user/logout/', UserLogout.as_view(), name='logout'),
    path('user/role/', UserRole.as_view(), name='get_user_role'),
]