# Generated by Django 3.0.4 on 2020-05-08 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20200508_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='published',
        ),
    ]
