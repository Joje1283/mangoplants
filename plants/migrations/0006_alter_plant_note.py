# Generated by Django 3.2.6 on 2021-09-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_plant_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='note',
            field=models.TextField(default=''),
        ),
    ]
