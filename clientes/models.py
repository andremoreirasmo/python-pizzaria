from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, null=False, help_text='Nome')
    telephone = models.CharField(
        max_length=50, null=False, help_text='Telefone')
    address = models.CharField(
        max_length=300, null=False, help_text='Endereço')
    email = models.CharField(max_length=150, null=True, help_text='Email')

    def __str__(self):
        return self.name