# Generated by Django 3.2.6 on 2021-09-06 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('fecha', models.DateTimeField(verbose_name='fecha de lanzamiento')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portada', verbose_name='portada')),
                ('visitas', models.PositiveIntegerField()),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='libro.categoria')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo', 'fecha'],
            },
        ),
    ]