# Generated by Django 2.1.5 on 2019-05-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
