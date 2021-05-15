# Generated by Django 3.2.3 on 2021-05-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome', max_length=100, unique=True)),
                ('value', models.FloatField(help_text='Valor')),
                ('length', models.CharField(default='P', help_text='P - Pequena, M - Média, G - Grande', max_length=1)),
                ('detail', models.CharField(help_text='Sabor ou qualquer outra informação.', max_length=500, null=True)),
            ],
        ),
    ]