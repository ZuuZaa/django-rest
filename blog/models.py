from django.db import models

# Create your models here.
class BlogModel(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()

    def _str_(self):
        return f"{self.title}"