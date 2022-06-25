from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=150)
    message = models.TextField()
    
    def __str__(self):
        return self.email