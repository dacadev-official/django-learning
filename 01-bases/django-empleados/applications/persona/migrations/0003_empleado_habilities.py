# Generated by Django 3.2.6 on 2021-08-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210819_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilities',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
