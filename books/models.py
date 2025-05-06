from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class books(models.Model):
    book_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    condition = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50, default='Fiction')
    tags = models.TextField()
    language = models.CharField(max_length=20, default='English')
    location = models.CharField(max_length=50)
    exchange_option = models.CharField(max_length=50, default="Shipping")
    coverimage = models.ImageField(upload_to='book_images/')
    additional_image1 = models.ImageField(upload_to='book_images/')
    additional_image2 = models.ImageField(upload_to='book_images/')
    additional_image3 = models.ImageField(upload_to='book_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
