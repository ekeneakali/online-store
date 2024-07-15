
from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class SellingCategory(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'SellingCategory'


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to="category", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Category'



class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="document")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    discount = models.IntegerField(default=True)
    old = models.FloatField(default=True)
    price = models.IntegerField()
    num_site = models.IntegerField(default=0)
    created_by = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name_plural = 'Product'

    
    class Meta():
        ordering = ['-created_at',]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    upload = models.FileField(upload_to='profile_upload')
    description = models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return str(self.image)

    class Meta():
        verbose_name_plural = 'Profile'



class NewsLetter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=700)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Contact'

class Video_Category(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Video_Category'


class Video(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    video_upload = models.FileField(upload_to="video/")
    category = models.ForeignKey(Video_Category, on_delete=models.CASCADE, verbose_name='select_category')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Video'

    class Meta():
        ordering = ['-created_at',]

class ViewCount(models.Model):

    video = models.ForeignKey(Video, related_name='view_count', on_delete=models.CASCADE)

    ip_address = models.CharField(max_length=50)

    session = models.CharField(max_length=50)

    def __str__(self):

        return self.ip_address

    class Meta():
        verbose_name_plural = 'ViewCount'


    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    note = models.TextField(default=True)
    amount = models.CharField(max_length=100)
    cart_item = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    class Meta():
        verbose_name_plural = 'Order'








