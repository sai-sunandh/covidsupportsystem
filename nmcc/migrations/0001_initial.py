# Generated by Django 3.0 on 2021-06-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('MOBILE', models.IntegerField()),
                ('DISTRICT', models.CharField(max_length=30)),
            ],
        ),
    ]
