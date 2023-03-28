from django.db import models

from django.contrib.auth import get_user_model


class Task(models.Model):
    # Definindo os campos
    STATUS = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    task = models.CharField(max_length=255)
    done = models.CharField(
        max_length=6,
        choices=STATUS
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True) # sempre que algo for criado automaticamente insere a data
    final_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.task