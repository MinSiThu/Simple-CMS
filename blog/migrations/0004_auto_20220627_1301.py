# Generated by Django 3.2.13 on 2022-06-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_content_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
