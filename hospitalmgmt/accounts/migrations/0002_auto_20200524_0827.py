# Generated by Django 3.0.6 on 2020-05-24 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Patient', 'Patient'), ('HR', 'HR'), ('Doctor', 'Doctor'), ('Receptionist', 'Receptionist')], default='None', max_length=20),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('medication', models.CharField(max_length=100)),
                ('instruction', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
                ('cost', models.IntegerField(blank=True, default=0)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctors', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
