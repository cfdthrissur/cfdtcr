from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# create your models here.
# Genearl Details of LSGD
class D001(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    lsgd_name = models.CharField(max_length = 100, unique = True)
    lsgd_year_of_formation = models.IntegerField(null = True)
    lsgd_area_in_sqkm = models.FloatField(null = True)
    lsgd_taluk_name = models.CharField(max_length = 100, null = True)
    lsgd_block_name = models.CharField(max_length = 100, null = True)
    lsgd_parliamentary_constituency = models.CharField(max_length = 100, null = True) 
    lsgd_assembly_constituency = models.CharField(max_length = 100, null = True)
    lsgd_no_of_wards = models.IntegerField(null = True)
    lsgd_no_of_female_wards = models.IntegerField(null = True)
    lsgd_no_of_scst_wards = models.IntegerField(null = True)
    lsgd_no_of_rivers = models.IntegerField(null = True)
    lsgd_name_of_rivers = models.TextField(null = True)
    lsgd_coastal_line_length_in_km = models.FloatField(null = True)
    lsgd_forest_area_in_hectors = models.FloatField(null = True)
    lsgd_type_of_soil = models.CharField(max_length = 100, null = True)
    lsgd_main_roads = models.TextField(null = True)
    lsgd_nearest_railway_station = models.CharField(max_length = 100, null = True)
    lsgd_jilla_panchayath_name = models.CharField(max_length = 100, null = True)
    lsgd_jilla_panchayath_ward = models.CharField(max_length = 100, null = True)
    lsgd_block_panchayath_name = models.CharField(max_length = 100, null = True)
    lsgd_block_panchayath_wards = models.CharField(max_length = 100, null = True)

# Demographic particulars of LSGD
class D002(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    population_male = models.IntegerField(null = True)
    population_female = models.IntegerField(null = True)
    population_male_sc = models.IntegerField(null = True)
    population_female_sc = models.IntegerField(null = True)
    population_male_st = models.IntegerField(null = True)
    population_female_st = models.IntegerField(null = True)
    children_0_to_6_age_male = models.IntegerField(null = True)
    children_0_to_6_age_female = models.IntegerField(null = True)
    children_0_to_6_age_male_sc = models.IntegerField(null = True)
    children_0_to_6_age_female_sc = models.IntegerField(null = True)
    children_0_to_6_age_male_st = models.IntegerField(null = True)
    children_0_to_6_age_female_st = models.IntegerField(null = True)
    children_6_to_10_age_male = models.IntegerField(null = True)
    children_6_to_10_age_female = models.IntegerField(null = True)
    children_0_to_18_age_male = models.IntegerField(null = True)
    children_0_to_18_age_female = models.IntegerField(null = True)
    literates_male = models.IntegerField(null = True)
    literates_female = models.IntegerField(null = True)
    migrant_labours_male = models.IntegerField(null = True)
    migrant_labours_female = models.IntegerField(null = True)
    migrant_labours_child_male = models.IntegerField(null = True)
    migrant_labours_child_female = models.IntegerField(null = True)
    third_gender_persons = models.IntegerField(null = True)
    household_all = models.IntegerField(null = True)
    household_sc = models.IntegerField(null = True)
    household_st = models.IntegerField(null = True)
    bpl_families = models.IntegerField(null = True)

# Sex Desegregated Data of Children
class D003(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    children_male_below_age_1 = models.IntegerField(null = True)
    children_female_below_age_1 = models.IntegerField(null = True)
    children_male_1_to_3_age = models.IntegerField(null = True)
    children_female_1_to_3_age = models.IntegerField(null = True)
    children_male_3_to_5_age = models.IntegerField(null = True)
    children_female_3_to_5_age = models.IntegerField(null = True)
    children_male_5_to_6_age = models.IntegerField(null = True)
    children_female_5_to_6_age = models.IntegerField(null = True)
    children_male_6_to_10_age = models.IntegerField(null = True)
    children_female_6_to_10_age = models.IntegerField(null = True)
    children_male_10_to_18_age = models.IntegerField(null = True)
    children_female_10_to_18_age = models.IntegerField(null = True)

#Sex Wise Disability Data of Children
class D004(models.Model):
    lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
    Total_disabled_M = models.IntegerField(null = True)
    Total_disabled_F = models.IntegerField(null = True)
    Locomotrs_M = models.IntegerField(null = True)
    Locomotrs_F = models.IntegerField(null = True)
    Visual_dis_M = models.IntegerField(null = True)
    Visual_dis_F = models.IntegerField(null = True)
    Hearing_dis_M = models.IntegerField(null = True)
    Hearing_dis_F = models.IntegerField(null = True)
    MR_M = models.IntegerField(null = True)
    MR_F = models.IntegerField(null = True)
    Auttisam_M = models.IntegerField(null = True)
    Auttisam_F = models.IntegerField(null = True)
    Ceribral_Palsy_M = models.IntegerField(null = True)
    Ceribral_Palsy_F = models.IntegerField(null = True)
    Multiple_Disability_M = models.IntegerField(null = True)
    Multiple_Disability_F = models.IntegerField(null = True)
    Mentally_Ill_M = models.IntegerField(null = True)
    Mentally_Ill_F = models.IntegerField(null = True)
    Others_Disability_M = models.IntegerField(null = True)
    Others_Disability_F = models.IntegerField(null = True)
    NO_Dis_LSG_Scholarshiip_M = models.IntegerField(null = True)
    NO_Dis_LSG_Scholarshiip_F = models.IntegerField(null = True)
    Other_scholar_M = models.IntegerField(null = True)
    Other_scholar_F = models.IntegerField(null = True)
    CWD_M = models.IntegerField(null = True)
    CWD_F = models.IntegerField(null = True)
    RBSY_CHIS_M = models.IntegerField(null = True) 
    RBSY_CHIS_F = models.IntegerField(null = True)

class D005(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	M_Fully_Immunised = models.IntegerField(null = True)
	F_Fully_Immunised = models.IntegerField(null = True)
	M_Partially_Immunised = models.IntegerField(null = True)
	F_Partially_Immunised = models.IntegerField(null = True)
	M_Incidents_of_Diphtheria = models.IntegerField(null = True)
	F_Incidents_of_Diphtheria = models.IntegerField(null = True)
	M_Woopingcough = models.IntegerField(null = True)
	F_Woopingcough = models.IntegerField(null = True)
	M_Tetnus = models.IntegerField(null = True)
	F_Tetnus = models.IntegerField(null = True)
	M_TB = models.IntegerField(null = True)
	F_TB = models.IntegerField(null = True)
	M_Measelous = models.IntegerField(null = True)
	F_Measelous = models.IntegerField(null = True)
	M_Janundees = models.IntegerField(null = True)
	F_Janundees = models.IntegerField(null = True)
	M_Others = models.IntegerField(null = True)
	F_Others = models.IntegerField(null = True)
	M_Vitamine_A = models.IntegerField(null = True)
	F_Vitamine_A = models.IntegerField(null = True)
	M_IFA = models.IntegerField(null = True)
	F_IFA = models.IntegerField(null = True)
	M_Life_Style_Diesease = models.IntegerField(null = True)
	F_Life_Style_Diesease = models.IntegerField(null = True)
	cancer_M = models.IntegerField(null = True)
	cancer_F = models.IntegerField(null = True)
	CHD_M = models.IntegerField(null = True)
	CHD_F = models.IntegerField(null = True)
	DM_M = models.IntegerField(null = True)
	DM_F = models.IntegerField(null = True)
	BP_M = models.IntegerField(null = True)
	BP_F = models.IntegerField(null = True)
	M_Diaherroea = models.IntegerField(null = True)
	F_Diaherroea = models.IntegerField(null = True)
	M_RTI = models.IntegerField(null = True)
	F_RTI = models.IntegerField(null = True)
	M_Anemia = models.IntegerField(null = True)
	F_Anemia = models.IntegerField(null = True)
	worms_Infected_M = models.IntegerField(null = True)
	worms_Infected_F = models.IntegerField(null = True)
	Emotional_Behavivour_M = models.IntegerField(null = True)
	Emotional_Behavivour_F = models.IntegerField(null = True)

class D006(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Preg_Reg_in_Time_G = models.IntegerField(null = True)
	Preg_Reg_in_Time_SC = models.IntegerField(null = True)
	Preg_Reg_in_Time_ST = models.IntegerField(null = True)
	Preg_Reg_not_Time_G = models.IntegerField(null = True)
	Preg_Reg_not_Time_SC = models.IntegerField(null = True)
	Preg_Reg_not_Time_ST = models.IntegerField(null = True)
	JSSY_JSSK_G = models.IntegerField(null = True)
	JSSY_JSSK_SC = models.IntegerField(null = True)
	JSSY_JSSK_ST = models.IntegerField(null = True)
	Birth_Reg_in_Time_G = models.IntegerField(null = True)
	Birth_Reg_in_Time_SC = models.IntegerField(null = True)
	Birth_Reg_in_Time_ST = models.IntegerField(null = True)
	EBF_Mothers_G = models.IntegerField(null = True)
	EBF_Mothers_SC = models.IntegerField(null = True)
	EBF_Mothers_ST = models.IntegerField(null = True)
	IFA_Tablet_G = models.IntegerField(null = True)
	IFA_Tablet_SC = models.IntegerField(null = True)
	IFA_Tablet_ST = models.IntegerField(null = True)
	Risk_Preg_G = models.IntegerField(null = True)
	Risk_Preg_SC = models.IntegerField(null = True)
	Risk_Preg_ST = models.IntegerField(null = True)
	Still_Birth_G = models.IntegerField(null = True)
	Still_Birth_SC = models.IntegerField(null = True)
	Still_Birth_ST = models.IntegerField(null = True)
	Twins_G = models.IntegerField(null = True)
	Twins_SC = models.IntegerField(null = True)
	Twins_ST = models.IntegerField(null = True)
	Institu_Delivery_G = models.IntegerField(null = True)
	Institu_Delivery_SC = models.IntegerField(null = True)
	Institu_Delivery_ST = models.IntegerField(null = True)
	Comple_Maternal_Health_Checkup_G = models.IntegerField(null = True)
	Comple_Maternal_Health_Checkup_SC = models.IntegerField(null = True)
	Comple_Maternal_Health_Checkup_ST = models.IntegerField(null = True)
	Women_SNP_G = models.IntegerField(null = True)
	Women_SNP_SC = models.IntegerField(null = True)
	Women_SNP_ST = models.IntegerField(null = True)
	Maternal_Death_G = models.IntegerField(null = True)
	Maternal_Death_SC = models.IntegerField(null = True)
	Maternal_Death_ST = models.IntegerField(null = True)
	MTP_Abortion_G = models.IntegerField(null = True)
	MTP_Abortion_SC = models.IntegerField(null = True)
	MTP_Abortion_ST = models.IntegerField(null = True)
	Couples_Without_Children_G = models.IntegerField(null = True)
	Couples_Without_Children_SC = models.IntegerField(null = True)
	Couples_Without_Children_ST = models.IntegerField(null = True)


class D007(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	S_7_Live_Birth_G = models.IntegerField(null = True)
	S_7_Live_Birth_SC = models.IntegerField(null = True)
	S_7_Live_Birth_ST = models.IntegerField(null = True)
	S_7_Neonatal_Death_0_28day_G = models.IntegerField(null = True)
	S_7_Neonatal_Death_0_28day_SC = models.IntegerField(null = True)
	S_7_Neonatal_Death_0_28day_ST = models.IntegerField(null = True)
	S_7_Infant_Mortality_0_1_G = models.IntegerField(null = True)
	S_7_Infant_Mortality_0_1_SC = models.IntegerField(null = True)
	S_7_Infant_Mortality_0_1_ST = models.IntegerField(null = True)
	S_7_Child_Mortality_1_5_G = models.IntegerField(null = True)
	S_7_Child_Mortality_1_5_SC = models.IntegerField(null = True)
	S_7_Child_Mortality_1_5_ST = models.IntegerField(null = True)
	S_7_Death_5_14_Year_G = models.IntegerField(null = True)
	S_7_Death_5_14_Year_SC = models.IntegerField(null = True)
	S_7_Death_5_14_Year_ST = models.IntegerField(null = True)
	S_7_Death_Above_14_Year_G = models.IntegerField(null = True)
	S_7_Death_Above_14_Year_SC = models.IntegerField(null = True)
	S_7_Death_Above_14_Year_ST = models.IntegerField(null = True)
	S_7_Commited_Suicide_G = models.IntegerField(null = True)
	S_7_Commited_Suicide_SC = models.IntegerField(null = True)
	S_7_Commited_Suicide_ST = models.IntegerField(null = True)

class D008(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Newborn_measured = models.IntegerField(null = True)
	Newborn_Normal = models.IntegerField(null = True)
	Newborn_Mild = models.IntegerField(null = True)
	Newborn_Moderate = models.IntegerField(null = True)
	Newborn_Severe = models.IntegerField(null = True)
	Under3_measured = models.IntegerField(null = True)
	Under3_Normal = models.IntegerField(null = True)
	Under3_Mild = models.IntegerField(null = True)
	Under3_Moderate = models.IntegerField(null = True)
	Under3_Severe = models.IntegerField(null = True)
	Three_5_measured = models.IntegerField(null = True)
	Three_5_Normal = models.IntegerField(null = True)
	Three_5_Mild = models.IntegerField(null = True)
	Three_5_Moderate = models.IntegerField(null = True)
	Three_5_Severe = models.IntegerField(null = True)
	Adolescent_measured = models.IntegerField(null = True)
	Adolescent_Normal = models.IntegerField(null = True)
	Adolescent_Mild = models.IntegerField(null = True)
	Adolescent_Moderate = models.IntegerField(null = True)
	Adolescent_Severe = models.IntegerField(null = True)
	Pregnant_measured = models.IntegerField(null = True)
	Pregnant_Normal = models.IntegerField(null = True)
	Pregnant_Mild = models.IntegerField(null = True)
	Pregnant_Moderate = models.IntegerField(null = True)
	Pregnant_Severe = models.IntegerField(null = True)

class D009(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Enrolled_AW_SNP = models.IntegerField(null = True)
	Entolled_Pre_school_AW = models.IntegerField(null = True)
	AW_Nutrition_3_5 = models.IntegerField(null = True)
	Enrolled_other_PreSchool = models.IntegerField(null = True)
	AW_Count = models.IntegerField(null = True)
	AW_Own_Bldg = models.IntegerField(null = True)
	AW_Temp_Bldg = models.IntegerField(null = True)
	AW_Toilet = models.IntegerField(null = True)
	AW_Drinking_Water = models.IntegerField(null = True)
	AW_Compound_Wall = models.IntegerField(null = True)
	AW_Management_Committee = models.IntegerField(null = True)
	AW_YoungMothers_Club = models.IntegerField(null = True)
	AW_With_CP = models.IntegerField(null = True)

class D010(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	LP_School_Govt = models.IntegerField(null = True)
	LP_School_LSG = models.IntegerField(null = True)
	LP_School_Aided = models.IntegerField(null = True)
	LP_School_Un_Aided = models.IntegerField(null = True)
	UP_School_Govt = models.IntegerField(null = True)
	UP_School_LSG = models.IntegerField(null = True)
	UP_School_Aided = models.IntegerField(null = True)
	UP_School_Un_Aided = models.IntegerField(null = True)
	High_School_Govt = models.IntegerField(null = True)
	High_School_LSG = models.IntegerField(null = True)
	High_School_Aided = models.IntegerField(null = True)
	High_School_Un_Aided = models.IntegerField(null = True)
	Higher_Secondary_Govt = models.IntegerField(null = True)
	Higher_Secondary_LSG = models.IntegerField(null = True)
	Higher_Secondary_Aided = models.IntegerField(null = True)
	Higher_Secondary_Un_Aided = models.IntegerField(null = True)
	Vocational_Higher_Secondary_Govt = models.IntegerField(null = True)
	Vocational_Higher_Secondary_LSG = models.IntegerField(null = True)
	Vocational_Higher_Secondary_Aided = models.IntegerField(null = True)
	Vocational_Higher_Secondary_Un_Aided = models.IntegerField(null = True)
	Open_School_Centers_Govt = models.IntegerField(null = True)
	Open_School_Centers_LSG = models.IntegerField(null = True)
	Open_School_Centers_Aided = models.IntegerField(null = True)
	Open_School_Centers_Un_Aided = models.IntegerField(null = True)
	Anganwadi_Centers_Govt = models.IntegerField(null = True)
	Anganwadi_Centers_LSG = models.IntegerField(null = True)
	Anganwadi_Centers_Aided = models.IntegerField(null = True)
	Anganwadi_Centers_Un_Aided = models.IntegerField(null = True)
	Nursery_Pre_Primary_Govt = models.IntegerField(null = True)
	Nursery_Pre_Primary_LSG = models.IntegerField(null = True)
	Nursery_Pre_Primary_Aided = models.IntegerField(null = True)
	Nursery_Pre_Primary_Un_Aided = models.IntegerField(null = True)

class D011(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Total_NoofSchool = models.IntegerField(null = True)
	Total_Students_M = models.IntegerField(null = True)
	Total_Students_F = models.IntegerField(null = True)
	Total_Student_Transfered_Out = models.IntegerField(null = True)
	Total_Students_Dropout = models.IntegerField(null = True)
	Total_Chronic_Absentees = models.IntegerField(null = True)
	Total_Dropout_SCST = models.IntegerField(null = True)
	Total_CWSN = models.IntegerField(null = True)
	Total_Children_LD = models.IntegerField(null = True)
	Total_CWD = models.IntegerField(null = True)

class D012(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	No_of_School = models.IntegerField(null = True)
	Buiding_Permanent = models.IntegerField(null = True)
	Buiding_Temperory = models.IntegerField(null = True)
	Smart_Class_Room = models.IntegerField(null = True)
	Barrier_Free_Status = models.IntegerField(null = True)
	Drinking_Water = models.IntegerField(null = True)
	Toilets = models.IntegerField(null = True)
	Waste_Disposal_Facility = models.IntegerField(null = True)
	Play_Ground_with_STD = models.IntegerField(null = True)
	Kitchen_Permanent = models.IntegerField(null = True)
	Kitchen_Temperory = models.IntegerField(null = True)
	School_With_Green_Initative = models.IntegerField(null = True)


class D013(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	PHC_Govt = models.IntegerField(null = True)
	PHC_Private = models.IntegerField(null = True)
	PHC_OP = models.IntegerField(null = True)
	PHC_IP = models.IntegerField(null = True)
	PHC_Labour = models.IntegerField(null = True)
	PHC_Infant_Treatment = models.IntegerField(null = True)
	PHC_Operation = models.IntegerField(null = True)
	Dispensary_Govt = models.IntegerField(null = True)
	Dispensary_Private = models.IntegerField(null = True)
	Dispensary_OP = models.IntegerField(null = True)
	Dispensary_IP = models.IntegerField(null = True)
	Dispensary_Labour = models.IntegerField(null = True)
	Dispensary_Infant_Treatment = models.IntegerField(null = True)
	Dispensary_Operation = models.IntegerField(null = True)
	Hospital_Govt = models.IntegerField(null = True)
	Hospital_Private = models.IntegerField(null = True)
	Hospital_OP = models.IntegerField(null = True)
	Hospital_IP = models.IntegerField(null = True)
	Hospital_Labour = models.IntegerField(null = True)
	Hospital_Infant_Treatment = models.IntegerField(null = True)
	Hospital_Operation = models.IntegerField(null = True)
	Jilla_Hospital_Govt = models.IntegerField(null = True)
	Jilla_Hospital_Private = models.IntegerField(null = True)
	Jilla_Hospital_OP = models.IntegerField(null = True)
	Jilla_Hospital_IP = models.IntegerField(null = True)
	Jilla_Hospital_Labour = models.IntegerField(null = True)
	Jilla_Hospital_Infant_Treatment = models.IntegerField(null = True)
	Jilla_Hospital_Operation = models.IntegerField(null = True)
	General_Hospital_Govt = models.IntegerField(null = True)
	General_Hospital_Private = models.IntegerField(null = True)
	General_Hospital_OP = models.IntegerField(null = True)
	General_Hospital_IP = models.IntegerField(null = True)
	General_Hospital_Labour = models.IntegerField(null = True)
	General_Hospital_Infant_Treatment = models.IntegerField(null = True)
	General_Hospital_Operation = models.IntegerField(null = True)
	Alopathy_Clinic_Govt = models.IntegerField(null = True)
	Alopathy_Clinic_Private = models.IntegerField(null = True)
	Alopathy_Clinic_OP = models.IntegerField(null = True)
	Alopathy_Clinic_IP = models.IntegerField(null = True)
	Alopathy_Clinic_Labour = models.IntegerField(null = True)
	Alopathy_Clinic_Infant_Treatment = models.IntegerField(null = True)
	Alopathy_Clinic_Operation = models.IntegerField(null = True)
	Ayurvedam_Govt = models.IntegerField(null = True)
	Ayurvedam_Private = models.IntegerField(null = True)
	Ayurvedam_OP = models.IntegerField(null = True)
	Ayurvedam_IP = models.IntegerField(null = True)
	Ayurvedam_Labour = models.IntegerField(null = True)
	Ayurvedam_Infant_Treatment = models.IntegerField(null = True)
	Ayurvedam_Operation = models.IntegerField(null = True)
	Homeo_Govt = models.IntegerField(null = True)
	Homeo_Private = models.IntegerField(null = True)
	Homeo_OP = models.IntegerField(null = True)
	Homeo_IP = models.IntegerField(null = True)
	Homeo_Labour = models.IntegerField(null = True)
	Homeo_Infant_Treatment = models.IntegerField(null = True)
	Homeo_Operation = models.IntegerField(null = True)
	Other_Ayush_Centers_Govt = models.IntegerField(null = True)
	Other_Ayush_Centers_Private = models.IntegerField(null = True)
	Other_Ayush_Centers_OP = models.IntegerField(null = True)
	Other_Ayush_Centers_IP = models.IntegerField(null = True)
	Other_Ayush_Centers_Labour = models.IntegerField(null = True)
	Other_Ayush_Centers_Infant_Treatment = models.IntegerField(null = True)
	Other_Ayush_Centers_Operation = models.IntegerField(null = True)
	MCH_Govt = models.IntegerField(null = True)
	MCH_Private = models.IntegerField(null = True)
	MCH_OP = models.IntegerField(null = True)
	MCH_IP = models.IntegerField(null = True)
	MCH_Labour = models.IntegerField(null = True)
	MCH_Infant_Treatment = models.IntegerField(null = True)
	MCH_Operation = models.IntegerField(null = True)

class D014(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Disability_Management_Institution = models.IntegerField(null = True)
	Disability_Management_Govt = models.IntegerField(null = True)
	Disability_Management_LSG = models.IntegerField(null = True)
	Disability_Management_NGO = models.IntegerField(null = True)
	Disability_Management_Private = models.IntegerField(null = True)
	Mental_Health_Institution = models.IntegerField(null = True)
	Mental_Health_Govt = models.IntegerField(null = True)
	Mental_Health_LSG = models.IntegerField(null = True)
	Mental_Health_NGO = models.IntegerField(null = True)
	Mental_Health_Private = models.IntegerField(null = True)
	Special_Education_Institution = models.IntegerField(null = True)
	Special_Education_Govt = models.IntegerField(null = True)
	Special_Education_LSG = models.IntegerField(null = True)
	Special_Education_NGO = models.IntegerField(null = True)
	Special_Education_Private = models.IntegerField(null = True)
	Institutional_Care_Institution = models.IntegerField(null = True)
	Institutional_Care_Govt = models.IntegerField(null = True)
	Institutional_Care_LSG = models.IntegerField(null = True)
	Institutional_Care_NGO = models.IntegerField(null = True)
	Institutional_Care_Private = models.IntegerField(null = True)
	Protection_Services_Institution = models.IntegerField(null = True)
	Protection_Services_Govt = models.IntegerField(null = True)
	Protection_Services_LSG = models.IntegerField(null = True)
	Protection_Services_NGO = models.IntegerField(null = True)
	Protection_Services_Private = models.IntegerField(null = True)
	Scanning_Centre_Institution = models.IntegerField(null = True)
	Scanning_Centre_Govt = models.IntegerField(null = True)
	Scanning_Centre_LSG = models.IntegerField(null = True)
	Scanning_Centre_NGO = models.IntegerField(null = True)
	Scanning_Centre_Private = models.IntegerField(null = True)
	Theraphy_Centre_Institution = models.IntegerField(null = True)
	Theraphy_Centre_Govt = models.IntegerField(null = True)
	Theraphy_Centre_LSG = models.IntegerField(null = True)
	Theraphy_Centre_NGO = models.IntegerField(null = True)
	Theraphy_Centre_Private = models.IntegerField(null = True)
	Palliataive_Care_Institution = models.IntegerField(null = True)
	Palliataive_Care_Govt = models.IntegerField(null = True)
	Palliataive_Care_LSG = models.IntegerField(null = True)
	Palliataive_Care_NGO = models.IntegerField(null = True)
	Palliataive_Care_Private = models.IntegerField(null = True)
	Clinical_Lab_Institution = models.IntegerField(null = True)
	Clinical_Lab_Govt = models.IntegerField(null = True)
	Clinical_Lab_LSG = models.IntegerField(null = True)
	Clinical_Lab_NGO = models.IntegerField(null = True)
	Clinical_Lab_Private = models.IntegerField(null = True)
	Deaddition_Centres_Institution = models.IntegerField(null = True)
	Deaddition_Centres_Govt = models.IntegerField(null = True)
	Deaddition_Centres_LSG = models.IntegerField(null = True)
	Deaddition_Centres_NGO = models.IntegerField(null = True)
	Deaddition_Centres_Private = models.IntegerField(null = True)

class D015(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	No_of_SC_Household = models.IntegerField(null = True)
	No_of_ST_Household = models.IntegerField(null = True)
	Ashraya_Family = models.IntegerField(null = True)
	Single_Room_Household = models.IntegerField(null = True)
	Un_Electrified_Household = models.IntegerField(null = True)
	Household_Without_DrinkingWater = models.IntegerField(null = True)
	Household_Without_Toilet = models.IntegerField(null = True)
	Public_Place_Without_Waste_Disposal = models.IntegerField(null = True)
	Homless_Family = models.IntegerField(null = True)
	Children_Exposed_to_Abuse = models.IntegerField(null = True)

class D016(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Under_Orphanges = models.IntegerField(null = True)
	Under_Premetric_Hostel = models.IntegerField(null = True)
	Missing = models.IntegerField(null = True)
	Conflict_with_Law = models.IntegerField(null = True)
	Children_Under_CWC = models.IntegerField(null = True)
	POCSO_Cases = models.IntegerField(null = True)
	At_Risk = models.IntegerField(null = True)
	Adopted = models.IntegerField(null = True)
	Foster_Care_Sponsorship = models.IntegerField(null = True)
	Road_Accidents = models.IntegerField(null = True)
	Calamities = models.IntegerField(null = True)
	Orphant_Children = models.IntegerField(null = True)
	HIV_Effected_Family = models.IntegerField(null = True)
	Migrant_Labours = models.IntegerField(null = True)
	Diability = models.IntegerField(null = True)
	Bedridden = models.IntegerField(null = True)
	Child_Labour = models.IntegerField(null = True)
	Child_Marriage = models.IntegerField(null = True)
	UnWed_Mothers = models.IntegerField(null = True)
	Physical_Punishment = models.IntegerField(null = True)

class D017(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Balasabha = models.IntegerField(null = True)
	Bala_Panchayat = models.IntegerField(null = True)
	AG_Club = models.IntegerField(null = True)
	AB_Club = models.IntegerField(null = True)
	Children_Gramasabha = models.IntegerField(null = True)
	Working_Group = models.IntegerField(null = True)
	School_Club = models.IntegerField(null = True)
	Vigilance_Committee = models.IntegerField(null = True)
	Social_Audit = models.IntegerField(null = True)

class D018(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Public_Library = models.IntegerField(null = True)
	Children_Library = models.IntegerField(null = True)
	AG_Club_at_AWC = models.IntegerField(null = True)
	Sports_Arts_Club = models.IntegerField(null = True)
	Cinema_Theatre = models.IntegerField(null = True)
	Cultural_Sports_Centre = models.IntegerField(null = True)
	Community_Hall = models.IntegerField(null = True)
	Children_Park = models.IntegerField(null = True)
	Play_Ground = models.IntegerField(null = True)
	Stadium = models.IntegerField(null = True)
	Swimming_Pool = models.IntegerField(null = True)

class D019(models.Model):
	lsgd_code_and_year = models.CharField(max_length = 20, unique = True, primary_key = True)
	Zero_Zone = models.IntegerField(null = True)
	Zebra_Crossing = models.IntegerField(null = True)
	School_Accident_Zone = models.IntegerField(null = True)
	Complaint_Box = models.IntegerField(null = True)
	Vigilance_Committee = models.IntegerField(null = True)
	Child_Friendly_Health_Institution = models.IntegerField(null = True)
	Model_Anganwadi = models.IntegerField(null = True)
	Jagrathasamithi = models.IntegerField(null = True)
	Playground_Upgraded = models.IntegerField(null = True)
	Public_Place_Upgraded = models.IntegerField(null = True)
	Stakeholder_Meeting = models.IntegerField(null = True)
	Public_Private_Coordination = models.IntegerField(null = True)
	Hospital_Development_Committee = models.IntegerField(null = True)
	VHNSC = models.IntegerField(null = True)
	VEC = models.IntegerField(null = True)
	PTA = models.IntegerField(null = True)
	ICDS_Coordination = models.IntegerField(null = True)
	SCST_SubCommittee = models.IntegerField(null = True)
	IEC_Material_Exbited_Vaccination = models.IntegerField(null = True)
