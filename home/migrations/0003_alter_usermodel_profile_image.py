# Generated by Django 4.1.5 on 2023-02-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_usermodel_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
