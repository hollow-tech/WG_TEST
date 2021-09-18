# Generated by Django 3.2.7 on 2021-09-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('file', models.FileField(upload_to='files/', verbose_name='файл')),
            ],
        ),
    ]
