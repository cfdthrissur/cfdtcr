# Generated by Django 2.0.6 on 2018-07-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d01_generaldetails',
            name='lsgd_area_in_sqkm',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='d01_generaldetails',
            name='lsgd_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='d01_generaldetails',
            name='lsgd_year_of_formation',
            field=models.IntegerField(null=True),
        ),
    ]
