from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "api"

urlpatterns = [
    path('users/', include('user_mgmt.api.urls'), name='user_api'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('books/', include('books.api.urls'), name='books_api'),
]