# Generated by Django 2.0.6 on 2018-08-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_remove_d004_rbsy_chis_f'),
    ]

    operations = [
        migrations.AddField(
            model_name='d004',
            name='RBSY_CHIS_F',
            field=models.IntegerField(null=True),
        ),
    ]
