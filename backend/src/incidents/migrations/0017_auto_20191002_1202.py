# Generated by Django 2.2.1 on 2019-10-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0016_incident_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='polictical_party',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='reported_through',
            field=models.CharField(default='GUEST', max_length=50),
        ),
    ]
