# Generated by Django 3.2 on 2023-02-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklistapp', '0005_review_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='overall_rating',
        ),
        migrations.AddField(
            model_name='book',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
