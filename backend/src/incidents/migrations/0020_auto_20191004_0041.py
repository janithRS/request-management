# Generated by Django 2.2.1 on 2019-10-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0019_auto_20191003_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentpolicereport',
            name='detained_vehicles',
            field=models.ManyToManyField(blank=True, related_name='incident_detained_vehicles', to='incidents.IncidentVehicle'),
        ),
        migrations.AddField(
            model_name='incidentpolicereport',
            name='respondents',
            field=models.ManyToManyField(blank=True, related_name='incident_respondents', to='incidents.IncidentPerson'),
        ),
    ]
