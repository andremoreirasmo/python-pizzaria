# Generated by Django 3.2.3 on 2021-05-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
