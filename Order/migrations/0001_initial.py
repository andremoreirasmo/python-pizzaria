# Generated by Django 3.2.3 on 2021-05-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pizza', '0001_initial'),
        ('clientes', '0002_auto_20210515_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('value', models.FloatField()),
                ('status', models.CharField(default='P', help_text='P - Pendente, F - Finalizado', max_length=1)),
                ('clients', models.ManyToManyField(to='clientes.Client')),
                ('pizzas', models.ManyToManyField(to='Pizza.Pizza')),
            ],
        ),
    ]