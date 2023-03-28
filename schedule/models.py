from django.db import models

from django.contrib.auth import get_user_model


class Contacts(models.Model):
    # Definindo os campos

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name