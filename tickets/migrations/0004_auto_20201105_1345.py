# Generated by Django 3.1 on 2020-11-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_orderstable_requestedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstable',
            name='requestedtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
