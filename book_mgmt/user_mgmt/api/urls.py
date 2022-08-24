from django.urls import path

from user_mgmt.api.views import RegisterUserView

app_name = "api_users"

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register')
]