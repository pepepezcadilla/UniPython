# Generated by Django 4.2.7 on 2023-11-10 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipamiento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entidades.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entidades.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entrada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Entidades.entrada')),
            ],
        ),
    ]