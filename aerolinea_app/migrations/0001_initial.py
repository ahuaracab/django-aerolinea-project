# Generated by Django 3.1.7 on 2021-07-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=64)),
                ('destino', models.CharField(max_length=64)),
                ('duracion', models.IntegerField()),
            ],
        ),
    ]
