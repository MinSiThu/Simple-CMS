# Generated by Django 3.2.13 on 2022-06-26 08:29

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
