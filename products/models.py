from django.db import models

class Category(models.Model):
    # Stores the name of the category, up to 255 characters.
    name = models.CharField(max_length=255)
    # Optional descriptive text for the category.
    description = models.TextField(blank=True, help_text="Brief description of the category")

class Product(models.Model):
    # Product name, up to 255 characters.
    name = models.CharField(max_length=255)
    # Product price, stored with up to 6 digits and 2 decimal places.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # ForeignKey relationship to Category, with cascade delete.
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # Optional product description.
    description = models.TextField(blank=True)
    # Quantity of the product in stock.
    stock_quantity = models.IntegerField(default=0, help_text="Available stock for the product")
    # Boolean to indicate if the product is available for sale.
    available = models.BooleanField(default=True, help_text="Is the product currently available for sale?")
    # Auto-set the field to now when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    # Auto-set the field to now every time the object is saved.
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    # ForeignKey relationship to Product, with cascade delete.
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    # Text of the review.
    review_text = models.TextField()
    # Numerical rating.
    rating = models.IntegerField()
    # Optional name of the person who created the review.
    created_by = models.CharField(max_length=255, blank=True, help_text="Name of the reviewer")
    # Auto-set the field to now when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
