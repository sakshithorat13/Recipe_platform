# Generated by Django 5.0.6 on 2024-06-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.TextField(),
        ),
    ]
