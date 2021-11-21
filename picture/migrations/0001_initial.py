# Generated by Django 3.2.9 on 2021-11-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('short_bio', models.TextField(max_length=250)),
                ('profile_picture', models.ImageField(upload_to='photos')),
                ('email', models.EmailField(max_length=254)),
                ('language', models.CharField(choices=[{'Arabic', 'AR'}, {'English', 'EN'}], max_length=50)),
                ('creation_date', models.DateField()),
            ],
        ),
    ]