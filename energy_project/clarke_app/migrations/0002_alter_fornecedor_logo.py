# Generated by Django 5.0.1 on 2024-01-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clarke_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='logo',
            field=models.CharField(max_length=100),
        ),
    ]
