# Generated by Django 3.2 on 2022-08-19 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_author', to='books.author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
