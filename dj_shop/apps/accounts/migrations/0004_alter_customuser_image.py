# Generated by Django 4.1.4 on 2023-02-13 07:32

from django.db import migrations, models
import modules.file_upload_module


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_city_alter_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=modules.file_upload_module.FileUploader.upload_to, verbose_name='عکس کاربر'),
        ),
    ]
