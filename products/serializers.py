from rest_framework import serializers
from .models import Product, Category, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the Product model

    def validate_price(self, value):
        # Ensure the product price is not negative or zero
        if value < 0:
            raise serializers.ValidationError("The price cannot be negative.")
        elif value == 0:
            raise serializers.ValidationError("The price cannot be zero.")
        return value

    def validate_name(self, value):
        # Ensure the product name is at least 3 characters long
        if len(value) < 3:
            raise serializers.ValidationError("The product name must be at least 3 characters long.")
        return value

    def validate_stock_quantity(self, value):
        # Stock quantity must not be negative
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value

    def validate(self, data):
        # Prevent duplicate product names within the same category
        if Product.objects.filter(name=data['name'], category=data['category']).exists():
            raise serializers.ValidationError("This product name already exists in the specified category.")
        return data

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']  # Explicitly include description and nested products

    def validate_name(self, value):
        # Ensure the category name is at least 3 characters and unique
        if len(value) < 3:
            raise serializers.ValidationError("The category name must be at least 3 characters long.")
        elif Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("A category with this name already exists.")
        return value
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # Include all fields from the Review model

    def validate(self, data):
        # Validate the rating range and limit reviews per user per product
        user = data.get('created_by')
        product = data['product']
        num_reviews = Review.objects.filter(product=product, created_by=user).count()
        if data['rating'] < 1 or data['rating'] > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        elif num_reviews >= 5:
            raise serializers.ValidationError("You cannot submit more than 5 reviews for the same product.")
        return data
