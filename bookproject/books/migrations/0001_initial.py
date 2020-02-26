# Generated by Django 3.0.3 on 2020-02-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('title', models.CharField(max_length=128, verbose_name="Book's title")),
                ('publisher', models.CharField(max_length=64, verbose_name='Publisher')),
                ('author', models.CharField(max_length=64, verbose_name='Author')),
                ('pages', models.IntegerField(default=0, verbose_name='Pages')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]