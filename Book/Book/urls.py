from django.contrib import admin
from django.urls import path
from .controllers.bookControllers import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", BookListCreate.as_view()),
    path("books/<int:id>", BookRetrieveUpdateDestroy.as_view()),
]
