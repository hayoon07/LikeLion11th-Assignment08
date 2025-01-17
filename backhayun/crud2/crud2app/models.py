from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    author = models.CharField(max_length=20)
    age = models.PositiveIntegerField(help_text="User Age")

    def __str__(self):
        return self.title