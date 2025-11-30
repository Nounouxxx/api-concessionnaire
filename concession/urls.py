from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
# Concessionnaires
path('concessionnaires/', views.ConcessionnaireList.as_view(), name='concessionnaire-list'),
path('concessionnaires/<int:pk>/', views.ConcessionnaireDetail.as_view(), name='concessionnaire-detail'),


# Vehicules for a concessionnaire
path('concessionnaires/<int:concessionnaire_pk>/vehicules/', views.VehiculeListByConcessionnaire.as_view(), name='vehicule-list'),
path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:vehicule_pk>/', views.VehiculeDetail.as_view(), name='vehicule-detail'),


# Bonus: user creation
path('users/', views.UserCreate.as_view(), name='user-create'),


# JWT
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]