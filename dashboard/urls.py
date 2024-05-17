from django.urls import path
from .views import upload, home, book_tracker

urlpatterns = [
    path("", home, name="home"),
    path("upload", upload, name="dashboard"),
    path("book", book_tracker, name="book"),
]