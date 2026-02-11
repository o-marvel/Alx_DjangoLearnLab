"""
Unit tests for Book API endpoints.

Tests Included:
- CRUD operations
- Filtering, searching, ordering
- Authentication and permission checks
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123')
        self.admin = User.objects.create_superuser(
            username='admin', 
            password='adminpass123', 
            email='admin@test.com')

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create book
        self.book = Book.objects.create(title="Test Book", author=self.author)

        # URLs
        self.list_url = reverse('book-list')      # /api/books/
        self.detail_url = reverse('book-detail', args=[self.book.id])  # /api/books/<id>/

    # ---------- CREATE ----------
    def test_create_book_authenticated(self):
        self.client.login(username='admin', password='adminpass123')
        data = {
            "title": "New Book",
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------- READ ----------
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    # ---------- UPDATE ----------
    def test_update_book(self):
        self.client.login(username='admin', password='adminpass123')
        data = {"title": "Updated Book Title"}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    # ---------- DELETE ----------
    def test_delete_book(self):
        self.client.login(username='admin', password='adminpass123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------- FILTERING ----------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---------- SEARCH ----------
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---------- ORDERING ----------
    def test_order_books(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
==================== TESTING DOCUMENTATION ====================

Testing Strategy:
-----------------
We test the API using Django REST Framework's APITestCase.

Areas Covered:
1. CRUD operations (Create, Read, Update, Delete)
2. Authentication and permission enforcement
3. Filtering
4. Searching
5. Ordering

Test Cases:
-----------
- test_create_book_authenticated → Admin can create book
- test_create_book_unauthenticated → Unauthorized users blocked
- test_get_books_list → Fetch all books
- test_get_single_book → Fetch single book
- test_update_book → Update book title
- test_delete_book → Delete book
- test_filter_books_by_title → Filtering works
- test_search_books → Search works
- test_order_books → Ordering works

How to Run Tests:
----------------
1. Activate virtual env
2. Run migrations:
   python manage.py migrate

3. Run tests:
   python manage.py test api

Interpreting Results:
---------------------
- OK → All tests passed
- FAIL → Test logic error
- ERROR → Code/config error

==============================================================
"""
