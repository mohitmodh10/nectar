# Generated by Django 4.1.5 on 2023-03-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_image_id_productimagesmodel_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_dic',
            field=models.TextField(blank=True, null=True),
        ),
    ]
