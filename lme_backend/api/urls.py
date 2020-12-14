from django.urls import include, path
from rest_framework import routers
from users.views import UserListView
from portfolio.views import PortfolioViewSet, TransactionViewSet


router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)
router.register(r'transaction', TransactionViewSet)


urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls)),
]
