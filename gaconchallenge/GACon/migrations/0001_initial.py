# Generated by Django 4.1 on 2022-09-04 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=250)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Talks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('room', models.IntegerField()),
                ('speaker', models.ManyToManyField(to='GACon.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GACon.attendees')),
                ('talks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GACon.talks')),
            ],
        ),
    ]
