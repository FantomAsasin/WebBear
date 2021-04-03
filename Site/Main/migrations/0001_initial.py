# Generated by Django 3.1.4 on 2021-01-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('role', models.CharField(max_length=100, verbose_name='Роль')),
                ('img', models.ImageField(upload_to='Avatar', verbose_name='Изображение')),
            ],
        ),
    ]
