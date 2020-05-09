# Generated by Django 3.0.4 on 2020-05-09 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_news_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='course image', upload_to='course/', verbose_name='Course image:')),
                ('title', models.CharField(help_text='course title', max_length=200, verbose_name='Course name:')),
                ('description', models.TextField(help_text='course description', verbose_name='Course description:')),
                ('price', models.PositiveIntegerField(help_text='course price', verbose_name='Course price:')),
                ('category', models.CharField(help_text='course category', max_length=200, verbose_name='Course category:')),
            ],
        ),
        migrations.CreateModel(
            name='reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='reviewer photo', upload_to='review/', verbose_name='Reviewer photo:')),
                ('name', models.CharField(help_text='reviewer name', max_length=200, verbose_name='Reviewer name:')),
                ('email', models.EmailField(help_text='reviewer email', max_length=254, verbose_name='Reviewer email:')),
                ('review', models.TextField(help_text='reviewer message', verbose_name='Reviewer message:')),
                ('stars', models.PositiveSmallIntegerField(help_text='reviewer rating', verbose_name='Reviewer rating')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='tag',
        ),
        migrations.DeleteModel(
            name='tag',
        ),
    ]
