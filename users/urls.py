from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", views.UserListAPIView.as_view()),
    path("register/", views.CreateUserAPIView.as_view(), name="register"),
    path("<str:jamb_reg_num>/", views.SingleUserAPIView.as_view(), name="view_user"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutAPIView.as_view(), name='user_logout'),
]
