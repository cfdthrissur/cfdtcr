# Generated by Django 2.0.6 on 2018-08-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_delete_d004'),
    ]

    operations = [
        migrations.CreateModel(
            name='D004',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Total_disabled_M', models.IntegerField(null=True)),
                ('Total_disabled_F', models.IntegerField(null=True)),
            ],
        ),
    ]
