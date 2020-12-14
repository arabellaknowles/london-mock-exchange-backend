from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers
from users.views import UserListView
from portfolio.views import PortfolioViewSet, TransactionViewSet



router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet, basename='portfolios')

portfolio_router = routers.NestedSimpleRouter(router, r'portfolio', lookup='portfolio')
portfolio_router.register(r'transaction', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls)),
    path('', include(portfolio_router.urls)),
]
