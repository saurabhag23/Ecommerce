# Import necessary modules and views for routing
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ReviewViewSet, product_list, product_search, UserLoginView, UserLogoutView

# Create a router for automatically registering ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Register product endpoints
router.register(r'categories', CategoryViewSet)  # Register category endpoints
router.register(r'reviews', ReviewViewSet)  # Register review endpoints

# Define URL patterns for the project
urlpatterns = [
    # Include the router-generated URLs for products, categories, and reviews
    path('', include(router.urls)),
    
    # URL for listing products
    path('product-list/', product_list, name='product-list'),
    
    # URL for product search functionality
    path('search/', product_search, name='product_search'),
    
    # URL for user login
    path('login/', UserLoginView.as_view(), name='login'),
    
    # URL for user logout
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
