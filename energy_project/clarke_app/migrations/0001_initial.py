# Generated by Django 5.0.1 on 2024-01-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('logo', models.ImageField(default=None, upload_to='logos/')),
                ('estado_origem', models.CharField(default=None, max_length=50)),
                ('custo_por_kwh', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('limite_minimo_kwh', models.PositiveIntegerField()),
                ('numero_total_clientes', models.PositiveIntegerField()),
                ('avaliacao_media_clientes', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
