# Generated by Django 2.2 on 2019-05-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_glassfridgeimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhilipMorris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('diagonals', models.CharField(max_length=100)),
                ('sides', models.CharField(max_length=100)),
                ('positions', models.CharField(max_length=100)),
                ('positions_y', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
