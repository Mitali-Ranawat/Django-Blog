# Generated by Django 3.2.6 on 2021-08-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Post', max_length=255),
        ),
    ]
