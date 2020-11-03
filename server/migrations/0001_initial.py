# Generated by Django 3.1 on 2020-10-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_number', models.IntegerField(max_length=2)),
                ('num_tables', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_seats', models.IntegerField(max_length=2)),
                ('table_num', models.IntegerField(max_length=2)),
                ('available', models.BooleanField(default=True)),
                ('to_clean', models.BooleanField(default=False)),
            ],
        ),
    ]
