# Generated by Django 3.1.6 on 2021-03-27 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_ID', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('purpose', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('facility_ID', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mass_spectrometer',
            fields=[
                ('num_of_people_trained', models.IntegerField()),
                ('num_of_researchers', models.IntegerField()),
                ('num_of_publications', models.IntegerField()),
                ('num_of_samples', models.IntegerField()),
                ('equipment_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('facility_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareApp.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Fluorometer',
            fields=[
                ('num_of_people_trained', models.IntegerField()),
                ('num_of_researchers', models.IntegerField()),
                ('num_of_publications', models.IntegerField()),
                ('num_of_samples', models.IntegerField()),
                ('equipment_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('facility_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareApp.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Flow_cytometer',
            fields=[
                ('num_of_people_trained', models.IntegerField()),
                ('num_of_researchers', models.IntegerField()),
                ('num_of_publications', models.IntegerField()),
                ('num_of_samples', models.IntegerField()),
                ('equipment_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('facility_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareApp.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Confocal_microscope',
            fields=[
                ('num_of_people_trained', models.IntegerField()),
                ('num_of_researchers', models.IntegerField()),
                ('num_of_publications', models.IntegerField()),
                ('num_of_samples', models.IntegerField()),
                ('equipment_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('facility_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareApp.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Centrifuge',
            fields=[
                ('num_of_people_trained', models.IntegerField()),
                ('num_of_researchers', models.IntegerField()),
                ('num_of_publications', models.IntegerField()),
                ('num_of_samples', models.IntegerField()),
                ('equipment_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('facility_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareApp.facility')),
            ],
        ),
    ]
