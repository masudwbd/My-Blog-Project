# Generated by Django 3.2.5 on 2021-08-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0006_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]