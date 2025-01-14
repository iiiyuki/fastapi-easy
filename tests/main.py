import pytest
from fastapi.testclient import TestClient
from app import app, books_db, Book

client = TestClient(app)


# Helper function to create a test book
def create_test_book():
    return Book(id=3, title="Brave New World", author="Aldous Huxley", description="Dystopian novel", rating=8.9)


# Test cases
@pytest.mark.parametrize("test_input,expected", [
    ("/", {"message": "Welcome to the Book Management API!"}),
])
def test_read_root_returns_welcome_message(test_input, expected):
    response = client.get(test_input)
    assert response.status_code == 200
    assert response.json() == expected


def test_get_books_returns_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == len(books_db)


def test_get_book_by_id_returns_correct_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_book_by_id_returns_404_if_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}


def test_create_book_adds_new_book():
    new_book = create_test_book()
    response = client.post("/books", json=new_book.dict())
    assert response.status_code == 200
    assert response.json()["id"] == new_book.id


def test_create_book_returns_400_if_id_exists():
    new_book = create_test_book()
    books_db.append(new_book)  # Add the book manually to simulate conflict
    response = client.post("/books", json=new_book.dict())
    assert response.status_code == 400
    assert response.json() == {"detail": "Book with this ID already exists"}
    books_db.remove(new_book)  # Clean up after the test


def test_update_book_updates_existing_book():
    updated_book = create_test_book()
    response = client.put("/books/1", json=updated_book.dict())
    assert response.status_code == 200
    assert response.json()["id"] == updated_book.id


def test_update_book_returns_404_if_not_found():
    updated_book = create_test_book()
    response = client.put("/books/999", json=updated_book.dict())
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}


def test_delete_book_removes_book():
    response = client.delete("/books/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Book with ID 2 has been deleted"}


def test_delete_book_returns_404_if_not_found():
    response = client.delete("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
