from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio  = models.TextField(max_length=500)
    imags = models.ImageField(upload_tu='auhtors')
    def __str__(self):
        return self.name
    





class Post(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    content = models.TextField(max_length=15000)
    author = models.ForeignKey(Author,related_name='post_author',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    def __str__(self):
        return self.title
    