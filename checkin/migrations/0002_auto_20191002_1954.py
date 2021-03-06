# Generated by Django 2.2.5 on 2019-10-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='events',
            name='event_id',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
