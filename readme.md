# 🛒 E-commerce Product Management System

## 📋 Project Overview

This project is an **E-commerce Product Management System** that allows administrators to manage products and categories (add, update, and delete), while users can view and search for products by name or category. The system includes user authentication, pagination, and review management.

---

## 🛠️ Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates
- **Database**: SQLite (can be switched to PostgreSQL)
- **Testing**: Django's Test Framework (APIClient)
- **Authentication**: Django's built-in authentication system
- **API Testing**: Postman
- **Tools**: Docker (optional), Git, Postman

---

## 🌟 Key Features and Implementations

1. 📊 **Database Design**
   - Models: Product, Category, and Review
   - Implementation: Defined in `products/models.py`

2. 🔗 **ER Diagram**
   - Illustrates relationships between models
   - Implementation: Relationships implemented using ForeignKey fields

3. 🗃️ **Schema Development and Migrations**
   - Automatic schema generation using Django migrations
   - Implementation:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4. 🔍 **SQL Database Querying**
   - Dynamic querying for product filtering
   - Implementation: Product search view in `products/views.py`

5. ✏️ **CRUD Operations for Products and Categories**
   - Handled by `ProductViewSet` and `CategoryViewSet`
   - Implementation: In `products/views.py`

6. 🌐 **RESTful API Endpoints**
   - `/api/products/`: CRUD for products
   - `/api/categories/`: CRUD for categories
   - `/api/reviews/`: CRUD for reviews

7. 🖥️ **Django Template Language for Product Display**
   - Implementation: `product_list` function in `products/views.py`

8. 🔎 **Search Feature**
   - Users can search for products by name or category
   - Implementation: `product_search` function in `products/views.py`

9. 📄 **Pagination for Product Listings**
   - Implementation: Using Django REST Framework's built-in pagination

10. 🔐 **User Authentication and Authorization**
    - Implementation: `UserLoginView` and `UserLogoutView` in `products/views.py`

11. 🧪 **Testing the API**
    - Implementation: `CategoryTestCase` and `ReviewTestCase` in `products/tests.py`

12. ⚠️ **Error Handling and Validation**
    - Custom validations in serializers (`products/serializers.py`)

---

## 🚀 How to Run the Project Locally

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd ecommerce
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:** Open your browser and go to `http://127.0.0.1:8000/`.

---

## 🔗 API Endpoints

- 📦 Product API: `/api/products/`
- 🏷️ Category API: `/api/categories/`
- ⭐ Review API: `/api/reviews/`
- 🔍 Search Products: `/search/`

---

## 🎯 Conclusion

This project implements an e-commerce product management system with full CRUD functionality, RESTful API endpoints, user authentication, and custom error handling, making it a comprehensive solution for managing product catalogs. All features have been tested thoroughly using both automated tests and manual tools like Postman.

---

## 📬 Contact

For any questions or feedback, please reach out to Saurabh Agrawal at agrawalsaurabh916@gmail.com.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
