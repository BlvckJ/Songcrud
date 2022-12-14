# Generated by Django 4.1.2 on 2022-10-27 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('date_released', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField()),
                ('artiste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste')),
            ],
        ),
    ]
