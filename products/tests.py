from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import json

class CategoryTestCase(APIClient):
    def test_duplicate_category(self):
        # Create a new category named 'Electronics'
        self.client.post(reverse('category-list'), {'name': 'Electronics'})
        
        # Attempt to create the same category again, which should raise an error
        response = self.client.post(reverse('category-list'), {'name': 'Electronics'})
        
        # Ensure that a 400 Bad Request status is returned
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Check if the appropriate error message is included in the response
        self.assertIn('A category with this name already exists.', response.data)

class ReviewTestCase(APIClient):
    def test_excessive_reviews(self):
        # Set up a product ID and user for the review tests
        product_id = 1
        user = 'user1'
        
        # URL for the review list endpoint
        url = reverse('review-list')
        
        # Post 5 valid reviews for the same product and user
        for _ in range(5):
            self.client.post(url, {'product': product_id, 'created_by': user, 'rating': 4, 'review_text': 'Nice!'})
        
        # Try to post a 6th review, which should exceed the allowed limit
        response = self.client.post(url, {'product': product_id, 'created_by': user, 'rating': 5, 'review_text': 'Great!'})
        
        # Ensure that a 400 Bad Request status is returned due to excessive reviews
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Check if the appropriate error message is included in the response
        self.assertIn('You cannot submit more than 5 reviews for the same product.', response.data)
