from django.db import models
class Shows(models.Model):
    title=models.CharField(max_length=245)
    network=models.CharField(max_length=255)
    release_date=models.DateField(blank=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)