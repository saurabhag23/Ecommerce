E-commerce Product Management System
Project Overview
This project is an E-commerce Product Management System that allows administrators to manage products and categories (add, update, and delete), while users can view and search for products by name or category. The system also includes features for user authentication, pagination, and review management.

Technologies Used
Backend: Django, Django REST Framework
Frontend: Django Templates
Database: SQLite (Can be switched to PostgreSQL)
Testing: Django's Test Framework (APIClient)
Authentication: Django's built-in authentication system
API Testing: Postman
Tools: Docker (optional), Git, Postman
Key Features and Implementations
1. Database Design
Models: The system includes three main models: Product, Category, and Review.

The Product model stores product details, including name, price, category, description, stock quantity, availability, and timestamps.
The Category model stores category details, and each category can have multiple products.
The Review model allows users to leave reviews for products, with rating and text fields.
Implementation: Models are defined in products/models.py.

Each model is linked using ForeignKey relationships to ensure proper data integrity.
Models also include appropriate validation logic for fields such as price, stock, and product name length, ensuring the correctness of data stored in the database.
2. ER Diagram
ER Diagram: The relationships between the Product, Category, and Review models were illustrated in an ER diagram.

Categories have a one-to-many relationship with Products.
Products have a one-to-many relationship with Reviews.
Implementation: The relationships are implemented using ForeignKey fields in products/models.py.

3. Schema Development and Migrations
Schema Development: Django’s models were used to automatically generate the schema for the database using migrations.

The models include relationships between Product, Category, and Review.
Implementation:

The migrations were created using python manage.py makemigrations.
The schema was applied using python manage.py migrate.
4. SQL Database Querying
Queries: The project supports dynamic SQL querying by filtering products by category or name.

Products can be searched based on user input in the search bar.
Implementation:

The product_search view in products/views.py performs filtering using Django’s ORM, allowing flexible querying of product data using icontains for case-insensitive matching.
5. CRUD Operations for Products and Categories
CRUD Operations: The system allows administrators to create, retrieve, update, and delete products and categories.

Implementation:

These operations are handled by ProductViewSet and CategoryViewSet in products/views.py, which are registered in the urls.py using Django REST Framework’s DefaultRouter for automatic route generation.
CRUD operations are tested using API calls with tools like Postman.
6. RESTful API Endpoints
API Endpoints: The following API endpoints were created for products and categories:

/api/products/: Handles all CRUD operations for products.
/api/categories/: Handles all CRUD operations for categories.
/api/reviews/: Handles all CRUD operations for reviews.
Implementation:

These endpoints were set up using Django REST Framework’s ViewSet classes for Product, Category, and Review in products/views.py.
Serialization of the data is handled using ProductSerializer, CategorySerializer, and ReviewSerializer.
7. Django Template Language for Product Display
Product Display: Products are displayed using Django Templates. Users can view a list of available products on the frontend.

Implementation:

The product_list function in products/views.py fetches all products from the database and renders them using the product_list.html template located in products/templates/products/.
Each product is displayed along with its price, description, and category.
8. Search Feature
Search: Users can search for products by name or category through a search form.

Implementation:

The product_search function in products/views.py performs a search on both product names and categories using Django’s ORM.
The results are displayed in the product_list.html template.
9. Pagination for Product Listings
Pagination: Large product lists are paginated to improve usability.

Implementation:

Pagination was handled using Django REST Framework’s built-in pagination system. Pagination settings can be configured in the project’s settings file.
10. User Authentication and Authorization
Authentication: User login and logout functionality is provided. Administrators can manage products and categories, while regular users can only view and search.

Implementation:

The UserLoginView and UserLogoutView classes in products/views.py handle login and logout using Django’s built-in authentication system.
Authorization is enforced using LoginRequiredMixin and UserPassesTestMixin where necessary to restrict access to administrative functions.
11. Testing the API
API Testing: API endpoints were tested for proper functionality using Django’s APIClient in test cases.

Implementation:

CategoryTestCase and ReviewTestCase in products/tests.py test various scenarios, such as duplicate category creation and excessive reviews for a product.
Tests verify that appropriate error messages and HTTP status codes are returned.
12. Error Handling and Validation
Custom Error Handling: Custom validation ensures data integrity for product name uniqueness, price validation, stock quantity, and review limits.

Implementation:

Custom validations were added in the ProductSerializer, CategorySerializer, and ReviewSerializer in products/serializers.py to enforce rules such as ensuring a valid price, limiting the number of reviews a user can submit, and checking for duplicate products.
How to Run the Project Locally
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd ecommerce
Set Up a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application: Open your browser and go to http://127.0.0.1:8000/.

API Endpoints
Product API: /api/products/
Category API: /api/categories/
Review API: /api/reviews/
Search Products: /search/
Conclusion
This project implements an e-commerce product management system with full CRUD functionality, RESTful API endpoints, user authentication, and custom error handling, making it a comprehensive solution for managing product catalogs. All features have been tested thoroughly using both automated tests and manual tools like Postman.

