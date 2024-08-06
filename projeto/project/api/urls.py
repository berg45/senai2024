from django.urls import path, include
from . import views
from .views import ClientsListCreate, ClientsDetail, protected_view,  show_curl_command, get_token_view
import rest_framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    )
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
            title="API Documentação",
            default_version='v1',
            description="Documentação da API",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contato@minhaapi.com"),
            license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )


urlpatterns = [
    path('auth/', include('rest_framework.urls')),  
    path('posts/', ClientsListCreate.as_view(), name='clients-list-create'),
    path('posts/<int:pk>/', ClientsDetail.as_view(), name='post-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('curl/', show_curl_command, name='curl_command'),
    path('show-tokens/', get_token_view, name='show_tokens'),
    path('protected/', protected_view, name='protected'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

