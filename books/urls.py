from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('book_upload/', views.book_upload, name='book-upload'),
    path('book-details/<int:book_id>/', views.book_details ,name='book-details'),
    path('catalog/', views.catalog, name='catalog')
]

