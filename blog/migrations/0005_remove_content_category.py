# Generated by Django 3.2.13 on 2022-06-27 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220627_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='category',
        ),
    ]
