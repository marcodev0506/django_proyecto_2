# Generated by Django 4.2.16 on 2024-10-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Descripción',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300, null=True, verbose_name='Descripción'),
        ),
    ]
