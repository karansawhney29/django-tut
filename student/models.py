from django.db import models

# Create Student Model


class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True, max_length=254)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # When it was create
    updated_at = models.DateTimeField(auto_now=True)  # When i was update


