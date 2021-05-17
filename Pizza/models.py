from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Nome')
    value = models.FloatField(null=False, help_text='Valor')
    detail = models.CharField(
        max_length=500, help_text='Sabor ou qualquer outra informação.', null=True)
    photo = models.ImageField(upload_to='media', default='media/default.jpg')

    def __str__(self):
        return self.name