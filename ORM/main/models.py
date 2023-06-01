from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=2064)
    contant = models.TextField()
    image = models.ImageField(upload_to='images/', default="images/default.png")
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()
    # late_update = models.DateTimeField()