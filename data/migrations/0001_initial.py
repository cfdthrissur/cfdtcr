# Generated by Django 2.0.6 on 2018-06-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='D01_GeneralDetails',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('lsgd_name', models.CharField(max_length=100)),
                ('lsgd_year_of_formation', models.IntegerField()),
                ('lsgd_area_in_sqkm', models.FloatField()),
            ],
        ),
    ]
