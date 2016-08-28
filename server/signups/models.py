"""Model definitions."""
from django.db import models

class Signup(models.Model):
    """Model definition for each individual signup."""
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
