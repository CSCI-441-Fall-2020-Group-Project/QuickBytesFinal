# Generated by Django 3.1 on 2020-10-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='time_placed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
