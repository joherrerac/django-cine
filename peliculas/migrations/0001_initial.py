# Generated by Django 4.2 on 2023-04-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('duracion', models.DurationField(max_length=3)),
                ('productora', models.CharField(max_length=100)),
                ('fecha_estreno', models.DateField()),
            ],
        ),
    ]