# Generated by Django 2.2.13 on 2021-07-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('Phone', models.IntegerField(default='')),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FLIGHT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('gender1', models.CharField(default='', max_length=50)),
                ('from_city', models.CharField(default='', max_length=50)),
                ('to_city', models.CharField(default='', max_length=50)),
                ('from_date', models.DateField(default='')),
                ('to_date', models.DateField(default='')),
                ('rooms', models.BigIntegerField(default='')),
                ('adults', models.IntegerField(default='')),
                ('children', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='HOTEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('from_date', models.DateField(default='')),
                ('to_date', models.DateField(default='')),
                ('rooms', models.BigIntegerField(default='')),
                ('adults', models.IntegerField(default='')),
                ('children', models.IntegerField(default='')),
                ('email', models.EmailField(default='', max_length=254)),
                ('Phone', models.IntegerField(default='')),
            ],
        ),
    ]
