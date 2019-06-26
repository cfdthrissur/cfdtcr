# Generated by Django 2.0.6 on 2018-08-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_auto_20180807_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='D009',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Enrolled_AW_SNP', models.IntegerField(null=True)),
                ('Entolled_Pre_school_AW', models.IntegerField(null=True)),
                ('AW_Nutrition_3_5', models.IntegerField(null=True)),
                ('Enrolled_other_PreSchool', models.IntegerField(null=True)),
                ('AW_Count', models.IntegerField(null=True)),
                ('AW_Own_Bldg', models.IntegerField(null=True)),
                ('AW_Temp_Bldg', models.IntegerField(null=True)),
                ('AW_Toilet', models.IntegerField(null=True)),
                ('AW_Drinking_Water', models.IntegerField(null=True)),
                ('AW_Compound_Wall', models.IntegerField(null=True)),
                ('AW_Management_Committee', models.IntegerField(null=True)),
                ('AW_YoungMothers_Club', models.IntegerField(null=True)),
                ('AW_With_CP', models.IntegerField(null=True)),
            ],
        ),
    ]
