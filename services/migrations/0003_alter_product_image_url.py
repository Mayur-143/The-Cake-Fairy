# Generated by Django 4.2.6 on 2023-11-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(help_text="Relative path to the image within 'static/images/'", max_length=200),
        ),
    ]
