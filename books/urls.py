from django.urls import path
from .views import BookList, BookCreate, BookDelete, BookUpdate

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('create/', BookCreate.as_view(), name='book-create'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
]
