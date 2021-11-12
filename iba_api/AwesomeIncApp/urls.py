from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CustomerViewSet, ProductViewSet, ProductCategoryViewSet, InstallationViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'product_category', ProductCategoryViewSet, basename='product_category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'installations', InstallationViewSet, basename='installation')
urlpatterns = router.urls

