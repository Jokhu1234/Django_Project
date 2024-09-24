from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    slug = models.SlugField()
    link = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title