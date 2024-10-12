from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from App.views import CreateUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/',CreateUserView.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('api/', include('App.urls')),
    path('api_auth/',include('rest_framework.urls'))
    ]