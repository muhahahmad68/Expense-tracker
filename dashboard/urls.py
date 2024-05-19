from django.urls import path
from .views import upload, home, book_tracker, expense_analysis

urlpatterns = [
    path("", home, name="home"),
    path("upload", upload, name="dashboard"),
    path("book", book_tracker, name="book"),
    path('expense', expense_analysis, name='analysis'),
]
