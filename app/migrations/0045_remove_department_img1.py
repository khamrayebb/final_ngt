# Generated by Django 5.0.6 on 2025-06-26 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_rename_img2_department_img1_remove_department_img3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='img1',
        ),
    ]
