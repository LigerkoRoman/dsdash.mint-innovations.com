# Generated by Django 2.2 on 2019-05-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColaFridgeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.CharField(max_length=100)),
                ('green', models.CharField(max_length=100)),
                ('blue', models.CharField(max_length=100)),
                ('overall', models.CharField(max_length=100)),
            ],
        ),
    ]