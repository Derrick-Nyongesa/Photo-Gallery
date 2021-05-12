# Generated by Django 3.2.2 on 2021-05-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photo.category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photo.location'),
        ),
    ]
