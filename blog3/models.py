from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(("title"), max_length=50)
    body=models.TextField(("body"))
    def __str__(self):
        return self.title
    