# Generated by Django 4.1.4 on 2023-03-11 19:38

from django.db import migrations, models
import modules.file_upload_module


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=modules.file_upload_module.FileUploader.upload_to, verbose_name='عکس کاربر'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
