from django.db import models

# Create your models here.
class Books(models.Model):
    bookName=models.CharField(max_length=200)
    authorName=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    content=models.TextField()
    path=models.ImageField(upload_to="media/BooksImage")
    descr=models.CharField(max_length=500)
