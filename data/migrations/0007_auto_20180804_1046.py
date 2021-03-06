# Generated by Django 2.0.6 on 2018-08-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_delete_d03_sexdesegdataofchild'),
    ]

    operations = [
        migrations.CreateModel(
            name='D001',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('lsgd_name', models.CharField(max_length=100, unique=True)),
                ('lsgd_year_of_formation', models.IntegerField(null=True)),
                ('lsgd_area_in_sqkm', models.FloatField(null=True)),
                ('lsgd_taluk_name', models.CharField(max_length=100, null=True)),
                ('lsgd_block_name', models.CharField(max_length=100, null=True)),
                ('lsgd_parliamentary_constituency', models.CharField(max_length=100, null=True)),
                ('lsgd_assembly_constituency', models.CharField(max_length=100, null=True)),
                ('lsgd_no_of_wards', models.IntegerField(null=True)),
                ('lsgd_no_of_female_wards', models.IntegerField(null=True)),
                ('lsgd_no_of_scst_wards', models.IntegerField(null=True)),
                ('lsgd_no_of_rivers', models.IntegerField(null=True)),
                ('lsgd_name_of_rivers', models.TextField(null=True)),
                ('lsgd_coastal_line_length_in_km', models.FloatField(null=True)),
                ('lsgd_forest_area_in_hectors', models.FloatField(null=True)),
                ('lsgd_type_of_soil', models.CharField(max_length=100, null=True)),
                ('lsgd_main_roads', models.TextField(null=True)),
                ('lsgd_nearest_railway_station', models.CharField(max_length=100, null=True)),
                ('lsgd_jilla_panchayath_name', models.CharField(max_length=100, null=True)),
                ('lsgd_jilla_panchayath_ward', models.IntegerField(null=True)),
                ('lsgd_block_panchayath_name', models.CharField(max_length=100, null=True)),
                ('lsgd_block_panchayath_wards', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='D002',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('population_male', models.IntegerField(null=True)),
                ('population_female', models.IntegerField(null=True)),
                ('population_male_sc', models.IntegerField(null=True)),
                ('population_female_sc', models.IntegerField(null=True)),
                ('population_male_st', models.IntegerField(null=True)),
                ('population_female_st', models.IntegerField(null=True)),
                ('children_0_to_6_age_male', models.IntegerField(null=True)),
                ('children_0_to_6_age_female', models.IntegerField(null=True)),
                ('children_0_to_6_age_male_sc', models.IntegerField(null=True)),
                ('children_0_to_6_age_female_sc', models.IntegerField(null=True)),
                ('children_0_to_6_age_male_st', models.IntegerField(null=True)),
                ('children_0_to_6_age_female_st', models.IntegerField(null=True)),
                ('children_6_to_10_age_male', models.IntegerField(null=True)),
                ('children_6_to_10_age_female', models.IntegerField(null=True)),
                ('children_0_to_18_age_male', models.IntegerField(null=True)),
                ('children_0_to_18_age_female', models.IntegerField(null=True)),
                ('literates_male', models.IntegerField(null=True)),
                ('literates_female', models.IntegerField(null=True)),
                ('migrant_labours_male', models.IntegerField(null=True)),
                ('migrant_labours_female', models.IntegerField(null=True)),
                ('migrant_labours_child_male', models.IntegerField(null=True)),
                ('migrant_labours_child_female', models.IntegerField(null=True)),
                ('third_gender_persons', models.IntegerField(null=True)),
                ('household_all', models.IntegerField(null=True)),
                ('household_sc', models.IntegerField(null=True)),
                ('household_st', models.IntegerField(null=True)),
                ('bpl_families', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='D003',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('children_male_below_age_1', models.IntegerField(null=True)),
                ('children_female_below_age_1', models.IntegerField(null=True)),
                ('children_male_1_to_3_age', models.IntegerField(null=True)),
                ('children_female_1_to_3_age', models.IntegerField(null=True)),
                ('children_male_3_to_5_age', models.IntegerField(null=True)),
                ('children_female_3_to_5_age', models.IntegerField(null=True)),
                ('children_male_5_to_6_age', models.IntegerField(null=True)),
                ('children_female_5_to_6_age', models.IntegerField(null=True)),
                ('children_male_6_to_10_age', models.IntegerField(null=True)),
                ('children_female_6_to_10_age', models.IntegerField(null=True)),
                ('children_male_10_to_18_age', models.IntegerField(null=True)),
                ('children_female_10_to_18_age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='D004',
            fields=[
                ('lsgd_code_and_year', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Total_disabled_M', models.IntegerField(null=True)),
                ('Total_disabled_F', models.IntegerField(null=True)),
                ('Locomotrs_M', models.IntegerField(null=True)),
                ('Locomotrs_F', models.IntegerField(null=True)),
                ('Visual_dis_M', models.IntegerField(null=True)),
                ('Visual_dis_F', models.IntegerField(null=True)),
                ('Hearing_dis_M', models.IntegerField(null=True)),
                ('Hearing_dis_F', models.IntegerField(null=True)),
                ('MR_M', models.IntegerField(null=True)),
                ('MR_F', models.IntegerField(null=True)),
                ('Auttisam_M', models.IntegerField(null=True)),
                ('Auttisam_F', models.IntegerField(null=True)),
                ('Ceribral_Palsy_M', models.IntegerField(null=True)),
                ('Ceribral_Palsy_F', models.IntegerField(null=True)),
                ('Multiple_Disability_M', models.IntegerField(null=True)),
                ('Mentally_Ill_M', models.IntegerField(null=True)),
                ('Mentally_Ill_F', models.IntegerField(null=True)),
                ('Others_Disability_M', models.IntegerField(null=True)),
                ('Others_Disability_F', models.IntegerField(null=True)),
                ('NO_Dis_LSG_Scholarshiip_M', models.IntegerField(null=True)),
                ('NO_Dis_LSG_Scholarshiip_F', models.IntegerField(null=True)),
                ('Other_scholar_M', models.IntegerField(null=True)),
                ('Other_scholar_F', models.IntegerField(null=True)),
                ('CWD_M', models.IntegerField(null=True)),
                ('CWD_F', models.IntegerField(null=True)),
                ('RBSY_CHIS_M', models.IntegerField(null=True)),
                ('RBSY_CHIS_F', models.IntegerField(null=True)),
                ('RBSY_CHIS_t', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='D01_GeneralDetails',
        ),
    ]
