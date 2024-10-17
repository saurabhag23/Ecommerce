from django.contrib import admin
from .models import Product, Category, Review

# Register the Product model with Django admin to enable admin management.
admin.site.register(Product)

# Register the Category model with Django admin to allow admin interactions.
admin.site.register(Category)

# Register the Review model with Django admin, facilitating review management via admin.
admin.site.register(Review)

