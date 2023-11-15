# Generated by Django 4.2.6 on 2023-11-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_copia_delete_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plataforma',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Plataformas'},
        ),
        migrations.AlterModelOptions(
            name='videojuego',
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Videojuegos'},
        ),
        migrations.RenameField(
            model_name='videojuego',
            old_name='unidades',
            new_name='anio',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='existencias',
        ),
        migrations.RemoveField(
            model_name='videojuego',
            name='disponibilidad',
        ),
        migrations.AddField(
            model_name='plataforma',
            name='videojuego',
            field=models.ManyToManyField(to='main.videojuego'),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]