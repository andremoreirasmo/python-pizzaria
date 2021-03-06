# Generated by Django 3.2.3 on 2021-05-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome', max_length=100)),
                ('telephone', models.CharField(help_text='Telefone', max_length=50)),
                ('address', models.CharField(help_text='Endereço', max_length=300)),
                ('email', models.CharField(help_text='Email', max_length=150, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
