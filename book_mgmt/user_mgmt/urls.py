from django.urls import path
from user_mgmt.views import LoginUserView, RegisterView, UserLogoutView

app_name = "user_mgmt"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    
]