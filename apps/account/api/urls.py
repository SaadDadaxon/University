from django.urls import path
from .views import AccountRegisterViews, LoginViews, MyAccountViews, AccountRU
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenBlacklistView,
)


urlpatterns = [
    path('login/', LoginViews.as_view()),
    path('register/', AccountRegisterViews.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('my/account/', MyAccountViews.as_view()),
    path('my-account/retrive-update/<int:pk>/', AccountRU.as_view()),
]
