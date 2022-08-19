from django.urls import path
from user_mgmt.views import RegisterView

app_name = "user_mgmt"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    
]