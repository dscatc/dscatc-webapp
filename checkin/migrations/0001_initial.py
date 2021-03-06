# Generated by Django 2.2.5 on 2019-10-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=500)),
                ('event_name', models.CharField(max_length=100)),
                ('total_attendees', models.IntegerField(default=0)),
                ('check_in_count', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
