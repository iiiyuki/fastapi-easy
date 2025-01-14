from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# 创建 FastAPI 实例
app = FastAPI()


# 数据模型
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    rating: Optional[float] = None


# 模拟的数据库
books_db = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel", rating=9.4),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel", rating=9.1),
]


# 根路由
@app.get("/")
def read_root():
    """
    根路由
    :return:
    """
    return {"message": "Welcome to the Book Management API!"}


# 获取所有书籍
@app.get("/books", response_model=List[Book])
def get_books():
    """
    获取所有书籍
    :return:
    """
    return books_db


# 根据 ID 获取单本书
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    根据 ID 获取单本书
    :param book_id:
    :return:
        - success: value of book
        - fail: HTTPException(status_code=404, detail="Book not found")
    """
    pass


# 添加新书
@app.post("/books", response_model=Book)
def create_book(book: Book):
    """
    添加新书
    :param book:
    :return:
        - success: value of book
        - fail: HTTPException(status_code=400, detail="Book with this ID already exists")
    """
    pass


# 更新书籍信息
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    """
    更新书籍信息
    :param book_id:
    :param updated_book:
    :return:
        - success: value of updated_book
        - fail: HTTPException(status_code=404, detail="Book not found")
    """
    pass


# 删除书籍
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """
    删除书籍
    :param book_id:
    :return:
        - success: {"message": f"Book with ID {book_id} has been deleted"}
        - fail: HTTPException(status_code=404, detail="Book not found")
    """
    pass


@app.get("/lists")
def get_lists():
    """
    获取所有书籍
    :return:
    """
    pass


if __name__ == "__main__":
    import uvicorn

    # adapt to windows, using 127.0.0.1 not localhost
    uvicorn.run(app, host="127.0.0.1", port=8000)
