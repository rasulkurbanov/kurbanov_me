from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tag = models.ManyToManyField(Tag)
    excerpt = models.TextField()
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    

