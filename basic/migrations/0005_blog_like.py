# Generated by Django 4.2.20 on 2025-05-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_alter_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
