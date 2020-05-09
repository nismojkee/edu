# Generated by Django 3.0.4 on 2020-05-08 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='tag title', max_length=200, verbose_name='Tag title:')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='news image', upload_to='news/', verbose_name='News image:')),
                ('title', models.CharField(help_text='news title', max_length=200, verbose_name='News title:')),
                ('text', models.TextField(help_text='news text', verbose_name='News text:')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('tag', models.ForeignKey(help_text='news tag', on_delete=django.db.models.deletion.CASCADE, to='content.tag', verbose_name='Tag:')),
            ],
        ),
    ]