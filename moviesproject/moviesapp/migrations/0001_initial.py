# Generated by Django 4.2.3 on 2023-07-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_desc', models.TextField()),
                ('movie_year', models.IntegerField()),
            ],
        ),
    ]
