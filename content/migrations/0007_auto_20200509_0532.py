# Generated by Django 3.0.4 on 2020-05-09 02:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20200509_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='stars',
            field=models.PositiveSmallIntegerField(help_text='reviewer rating', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Reviewer rating'),
        ),
    ]