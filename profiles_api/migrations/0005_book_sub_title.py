# Generated by Django 3.0.3 on 2020-02-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_auto_20200205_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]