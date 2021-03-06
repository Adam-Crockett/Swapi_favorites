# Generated by Django 2.2.7 on 2020-01-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapi_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='id',
        ),
        migrations.AlterField(
            model_name='favorites',
            name='item_type',
            field=models.CharField(choices=[('films', 'Films'), ('people', 'People'), ('planets', 'Planets'), ('species', 'Species'), ('starships', 'Starships'), ('vehicles', 'Vehicles')], max_length=1),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
