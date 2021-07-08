# Generated by Django 3.1.7 on 2021-07-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arribos', to='aerolinea_app.aeropuerto'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='aerolinea_app.aeropuerto'),
        ),
    ]