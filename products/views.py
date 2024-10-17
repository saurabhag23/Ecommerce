from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.contrib.auth.views import LoginView, LogoutView

# Function to display the list of products on the frontend
def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Render the product list template and pass the products data
    return render(request, 'products/product_list.html', {'products': products})

# Function to handle product search by name or category
def product_search(request):
    # Get the search query from the request
    query = request.GET.get('q', '')
    if query:
        # Filter products by name or category containing the search query
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__name__icontains(query))
    else:
        # If no search query, fetch all products
        products = Product.objects.all()
    # Render the product list template with the filtered products
    return render(request, 'products/product_list.html', {'products': products})

# ViewSet for handling CRUD operations on Product model
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Fetch all products
    serializer_class = ProductSerializer  # Use the ProductSerializer for JSON serialization

# ViewSet for handling CRUD operations on Category model
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Fetch all categories
    serializer_class = CategorySerializer  # Use the CategorySerializer for JSON serialization

# ViewSet for handling CRUD operations on Review model
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Fetch all reviews
    serializer_class = ReviewSerializer  # Use the ReviewSerializer for JSON serialization

# View to handle user login using Django's built-in LoginView
class UserLoginView(LoginView):
    template_name = 'products/login.html'  # Template for login page
    redirect_authenticated_user = True  # Redirect already logged-in users

    # Redirect to the product list page after successful login
    def get_success_url(self):
        return reverse_lazy('product_list')

# View to handle user logout using Django's built-in LogoutView
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to the login page after logout
