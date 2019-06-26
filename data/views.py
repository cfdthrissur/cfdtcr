from django.shortcuts import render, redirect

from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd, Taluk, Block, Assembly, Parliament
from data.models import D001, D002, D003, D004, D005, D006, D007, D008, D009, D010, D011, D012, D013, D014, D015, D016, D017, D018, D019

from data.forms import F001, F002, F003, F004, F005, F006, F007, F008, F009, F010, F011, F012, F013, F014, F015, F016, F017, F018, F019
import xlrd

def toggle_lang(request):
    current_user = request.user
    if (current_user.profile.user_lang == 0):
        current_user.profile.user_lang = 1
    else:
        current_user.profile.user_lang = 0
    return render(request, 'data/success.html')    
    
def xl2sql(request):
    xls = Lsgd()
    loc = ("D:\cfdtcr\docs\data_transform.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(24)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        if (i==0):
            print ("conversion started")
        else:
            fld = sheet.row_values(i)
            xls.lsgd_code = fld[0]
            xls.lsgd_name = fld[1]
            xls.lsgd_type = fld[2]
            #xls.lsgd_taluk = fld[3]
            #xls.lsgd_block = fld[4]
            #xls.lsgd_district = fld[5]
            #xls.lsgd_assembly = fld[6]
            #xls.lsgd_parliament = fld[7]
            #xls.save()
            print (fld[0])
    return render(request, 'data/success.html')

# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D001 - General Details                                                               #
########################################################################################################################################################
def gdls_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q001").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    taluks = Taluk.objects.filter(taluk_code__startswith = district_code).values().order_by('taluk_code')
    blocks = Block.objects.filter(block_code__startswith = district_code).values().order_by('block_code')
    assemblys = Assembly.objects.filter(assembly_code__startswith = district_code).values().order_by('assembly_code')
    parliaments = Parliament.objects.filter(parliament_code__startswith = district_code).values().order_by('parliament_code')
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D001.objects.filter(lsgd_code_and_year = reqd_data )

    if request.method == 'POST':
        data_form01 = F001(request.POST)
        data01 = D001()
        print(request.POST)

        if data_form01.is_valid():
            data01.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data01.lsgd_name = data_form01.cleaned_data['lsgd_name']
            data01.lsgd_year_of_formation = data_form01.cleaned_data['lsgd_year_of_formation']
            data01.lsgd_area_in_sqkm = data_form01.cleaned_data['lsgd_area_in_sqkm']
            data01.lsgd_taluk_name = data_form01.cleaned_data['lsgd_taluk_name']
            data01.lsgd_block_name = data_form01.cleaned_data['lsgd_block_name']
            data01.lsgd_parliamentary_constituency = data_form01.cleaned_data['lsgd_parliamentary_constituency']
            data01.lsgd_assembly_constituency = data_form01.cleaned_data['lsgd_assembly_constituency']
            data01.lsgd_no_of_wards = data_form01.cleaned_data['lsgd_no_of_wards']
            data01.lsgd_no_of_female_wards = data_form01.cleaned_data['lsgd_no_of_female_wards']
            data01.lsgd_no_of_scst_wards = data_form01.cleaned_data['lsgd_no_of_scst_wards']
            data01.lsgd_no_of_rivers = data_form01.cleaned_data['lsgd_no_of_rivers']
            data01.lsgd_name_of_rivers = data_form01.cleaned_data['lsgd_name_of_rivers']
            data01.lsgd_coastal_line_length_in_km = data_form01.cleaned_data['lsgd_coastal_line_length_in_km']
            data01.lsgd_forest_area_in_hectors = data_form01.cleaned_data['lsgd_forest_area_in_hectors']
            data01.lsgd_type_of_soil = data_form01.cleaned_data['lsgd_type_of_soil']
            data01.lsgd_main_roads = data_form01.cleaned_data['lsgd_main_roads']
            data01.lsgd_nearest_railway_station = data_form01.cleaned_data['lsgd_nearest_railway_station']
            data01.lsgd_jilla_panchayath_name = data_form01.cleaned_data['lsgd_jilla_panchayath_name']
            data01.lsgd_jilla_panchayath_ward = data_form01.cleaned_data['lsgd_jilla_panchayath_ward']
            data01.lsgd_block_panchayath_name = data_form01.cleaned_data['lsgd_block_panchayath_name']
            data01.lsgd_block_panchayath_wards = data_form01.cleaned_data['lsgd_block_panchayath_wards']
            data01.save()
        
            print('Value saved')
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/demp/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/cfai/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/gdls.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments, 'answers': current_answerset})

    else:
        return render(request, 'data/gdlsm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments, 'answers': current_answerset})

########################################################################################################################################################
#                                                 Data Entry for D002 - Demographic Particulars                                                        #
########################################################################################################################################################
def demp_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q002").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D002.objects.filter(lsgd_code_and_year = reqd_data )

    if request.method == 'POST':
        data_form02 = F002(request.POST)
        data02 = D002()
        print(request.POST)

        if data_form02.is_valid():
            data02.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data02.population_male = data_form02.cleaned_data['population_male']
            data02.population_female = data_form02.cleaned_data['population_female']
            data02.population_male_sc = data_form02.cleaned_data['population_male_sc']
            data02.population_female_sc = data_form02.cleaned_data['population_female_sc']
            data02.population_male_st = data_form02.cleaned_data['population_male_st']
            data02.population_female_st = data_form02.cleaned_data['population_female_st']
            data02.children_0_to_6_age_male = data_form02.cleaned_data['children_0_to_6_age_male']
            data02.children_0_to_6_age_female = data_form02.cleaned_data['children_0_to_6_age_female']
            data02.children_0_to_6_age_male_sc = data_form02.cleaned_data['children_0_to_6_age_male_sc']
            data02.children_0_to_6_age_female_sc = data_form02.cleaned_data['children_0_to_6_age_female_sc']
            data02.children_0_to_6_age_male_st = data_form02.cleaned_data['children_0_to_6_age_male_st']
            data02.children_0_to_6_age_female_st = data_form02.cleaned_data['children_0_to_6_age_female_st']
            data02.children_6_to_10_age_male = data_form02.cleaned_data['children_6_to_10_age_male']
            data02.children_6_to_10_age_female = data_form02.cleaned_data['children_6_to_10_age_female']
            data02.children_0_to_18_age_male = data_form02.cleaned_data['children_0_to_18_age_male']
            data02.children_0_to_18_age_female = data_form02.cleaned_data['children_0_to_18_age_female']
            data02.literates_male = data_form02.cleaned_data['literates_male']
            data02.literates_female = data_form02.cleaned_data['literates_female']
            data02.migrant_labours_male = data_form02.cleaned_data['migrant_labours_male']
            data02.migrant_labours_female = data_form02.cleaned_data['migrant_labours_female']
            data02.migrant_labours_child_male = data_form02.cleaned_data['migrant_labours_child_male']
            data02.migrant_labours_child_female = data_form02.cleaned_data['migrant_labours_child_female']
            data02.third_gender_persons = data_form02.cleaned_data['third_gender_persons']
            data02.household_all = data_form02.cleaned_data['household_all']
            data02.household_sc = data_form02.cleaned_data['household_sc']
            data02.household_st = data_form02.cleaned_data['household_st']
            data02.bpl_families = data_form02.cleaned_data['bpl_families']
            data02.save()
            print("sucess data02")
        else:
            print("Form not valid")

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/sddc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/gdls/')

        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    if (current_user.profile.user_lang == 0):
        return render(request, 'data/02demp.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/02dempm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})


########################################################################################################################################################
#                                                Data Entry for D003 - Sex Desegragated Data of Children                                               #
########################################################################################################################################################

def sddc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    
    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q003").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D003.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form03 = F003(request.POST)
        data03 = D003()
        print(request.POST)

        if data_form03.is_valid():
            data03.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data03.children_male_below_age_1 = data_form03.cleaned_data['children_male_below_age_1']
            data03.children_female_below_age_1 = data_form03.cleaned_data['children_female_below_age_1']
            data03.children_male_1_to_3_age = data_form03.cleaned_data['children_male_1_to_3_age']
            data03.children_female_1_to_3_age = data_form03.cleaned_data['children_female_1_to_3_age']
            data03.children_male_3_to_5_age = data_form03.cleaned_data['children_male_3_to_5_age']
            data03.children_female_3_to_5_age = data_form03.cleaned_data['children_female_3_to_5_age']
            data03.children_male_5_to_6_age = data_form03.cleaned_data['children_male_5_to_6_age']
            data03.children_female_5_to_6_age = data_form03.cleaned_data['children_female_5_to_6_age']
            data03.children_male_6_to_10_age = data_form03.cleaned_data['children_male_6_to_10_age']
            data03.children_female_6_to_10_age = data_form03.cleaned_data['children_female_6_to_10_age']
            data03.children_male_10_to_18_age = data_form03.cleaned_data['children_male_10_to_18_age']
            data03.children_female_10_to_18_age = data_form03.cleaned_data['children_female_10_to_18_age']
            data03.save()
        
            print('SDDC Form saved')
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/swdd/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/demp/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/03sddc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/03sddcm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})




########################################################################################################################################################
#                                                Data Entry TEST -- One page Template -- Old Copy                                                      #
########################################################################################################################################################
def data_page(request):
    current_header = 1
    lsgd_code = 'KL008M001'
    data_entry_year = 2018
    current_user = request.user

    questions =  QuestionBank.objects.filter(question_code__startswith = "Q001").values().order_by('question_code')
    headers = QuestionHeader.objects.all().values()
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    current_header_text = headers[current_header-1].get('header_text')

    # Update the left column menu and related values.
    if request.method == 'POST':
        #print(request.POST)
        clicked_header = int(request.POST['clicked_header'])
        if clicked_header > 20 and 'next_page' in request.POST:
            current_header = clicked_header - 19
            if current_header > 19:
                current_header = 1
        elif clicked_header > 20 and 'prev_page' in request.POST:
            current_header = clicked_header - 21
            if current_header < 1:
                current_header = 19
        elif clicked_header > 20 and 'save_details' in request.POST:
            current_header = clicked_header - 20
        else:
            current_header = clicked_header
        
        current_header_text = headers[current_header-1].get('header_text')
        current_questions = "Q" + str('{0:03}'.format(current_header))
        #print(current_questions)
        questions =  QuestionBank.objects.filter(question_code__startswith = current_questions).values().order_by('question_code')

        # Enter current data into the database by collecting data from the current form.
        data_form = F001(request.POST)
        #print(data_form)
        #print(request.POST)
        
        if data_form.is_valid():
            print(data_form.cleaned_data['f1'])
        else:
            print("not valid")


    return render(request, 'data/data.html', {'headers': headers, 'current_header': current_header, 'current_header_text': current_header_text, \
                            'questions': questions, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user})

# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D004                                                            #
########################################################################################################################################################
def swdd_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q004").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D004.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form04 = F004(request.POST)
        data04 = D004()
        print(request.POST)

        if data_form04.is_valid():
            data04.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data04.Total_disabled_M = data_form04.cleaned_data['Total_disabled_M']
            data04.Total_disabled_F = data_form04.cleaned_data['Total_disabled_F']
            data04.Locomotrs_M = data_form04.cleaned_data['Locomotrs_M']
            data04.Locomotrs_F = data_form04.cleaned_data['Locomotrs_F']
            data04.Visual_dis_M = data_form04.cleaned_data['Visual_dis_M']
            data04.Visual_dis_F = data_form04.cleaned_data['Visual_dis_F']
            data04.Hearing_dis_M = data_form04.cleaned_data['Hearing_dis_M']
            data04.Hearing_dis_F = data_form04.cleaned_data['Hearing_dis_F']
            data04.MR_M = data_form04.cleaned_data['MR_M']
            data04.MR_F = data_form04.cleaned_data['MR_F']
            data04.Auttisam_M = data_form04.cleaned_data['Auttisam_M']
            data04.Auttisam_F = data_form04.cleaned_data['Auttisam_F']
            data04.Ceribral_Palsy_M = data_form04.cleaned_data['Ceribral_Palsy_M']
            data04.Ceribral_Palsy_F = data_form04.cleaned_data['Ceribral_Palsy_F']
            data04.Multiple_Disability_M = data_form04.cleaned_data['Multiple_Disability_M']
            data04.Multiple_Disability_F = data_form04.cleaned_data['Multiple_Disability_F']
            data04.Mentally_Ill_M = data_form04.cleaned_data['Mentally_Ill_M']
            data04.Mentally_Ill_F = data_form04.cleaned_data['Mentally_Ill_F']
            data04.Others_Disability_M = data_form04.cleaned_data['Others_Disability_M']
            data04.Others_Disability_F = data_form04.cleaned_data['Others_Disability_F']
            data04.NO_Dis_LSG_Scholarshiip_M = data_form04.cleaned_data['NO_Dis_LSG_Scholarshiip_M']
            data04.NO_Dis_LSG_Scholarshiip_F = data_form04.cleaned_data['NO_Dis_LSG_Scholarshiip_F']
            data04.Multiple_Disability_M = data_form04.cleaned_data['Multiple_Disability_M']
            data04.Multiple_Disability_F = data_form04.cleaned_data['Multiple_Disability_F']
            data04.Other_scholar_M = data_form04.cleaned_data['Other_scholar_M']
            data04.Other_scholar_F = data_form04.cleaned_data['Other_scholar_F']
            data04.CWD_M = data_form04.cleaned_data['CWD_M']
            data04.CWD_F = data_form04.cleaned_data['CWD_F']
            data04.RBSY_CHIS_M = data_form04.cleaned_data['RBSY_CHIS_M']
            data04.RBSY_CHIS_F = data_form04.cleaned_data['RBSY_CHIS_F']
            data04.save()
        
            print('Page validated and saved')
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/msc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/sddc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    if (current_user.profile.user_lang == 0):
        return render(request, 'data/swdd.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/swddm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
  
# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D004                                                            #
########################################################################################################################################################
def msc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q005").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D005.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form005 = F005(request.POST)
        data005 = D005()
        print(request.POST)

        if data_form005.is_valid():
            data005.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data005.M_Fully_Immunised = data_form005.cleaned_data['M_Fully_Immunised']
            data005.F_Fully_Immunised = data_form005.cleaned_data['F_Fully_Immunised']
            data005.M_Partially_Immunised = data_form005.cleaned_data['M_Partially_Immunised']
            data005.F_Partially_Immunised = data_form005.cleaned_data['F_Partially_Immunised']
            data005.M_Incidents_of_Diphtheria = data_form005.cleaned_data['M_Incidents_of_Diphtheria']
            data005.F_Incidents_of_Diphtheria = data_form005.cleaned_data['F_Incidents_of_Diphtheria']
            data005.M_Woopingcough = data_form005.cleaned_data['M_Woopingcough']
            data005.F_Woopingcough = data_form005.cleaned_data['F_Woopingcough']
            data005.M_Tetnus = data_form005.cleaned_data['M_Tetnus']
            data005.F_Tetnus = data_form005.cleaned_data['F_Tetnus']
            data005.M_TB = data_form005.cleaned_data['M_TB']
            data005.F_TB = data_form005.cleaned_data['F_TB']
            data005.M_Measelous = data_form005.cleaned_data['M_Measelous']
            data005.F_Measelous = data_form005.cleaned_data['F_Measelous']
            data005.M_Janundees = data_form005.cleaned_data['M_Janundees']
            data005.F_Janundees = data_form005.cleaned_data['F_Janundees']
            data005.M_Others = data_form005.cleaned_data['M_Others']
            data005.F_Others = data_form005.cleaned_data['F_Others']
            data005.M_Vitamine_A = data_form005.cleaned_data['M_Vitamine_A']
            data005.F_Vitamine_A = data_form005.cleaned_data['F_Vitamine_A']
            data005.M_IFA = data_form005.cleaned_data['M_IFA']
            data005.F_IFA = data_form005.cleaned_data['F_IFA']
            data005.M_Life_Style_Diesease = data_form005.cleaned_data['M_Life_Style_Diesease']
            data005.F_Life_Style_Diesease = data_form005.cleaned_data['F_Life_Style_Diesease']
            data005.cancer_M = data_form005.cleaned_data['cancer_M']
            data005.cancer_F = data_form005.cleaned_data['cancer_F']
            data005.CHD_M = data_form005.cleaned_data['CHD_M']
            data005.CHD_F = data_form005.cleaned_data['CHD_F']
            data005.DM_M = data_form005.cleaned_data['DM_M']
            data005.DM_F = data_form005.cleaned_data['DM_F']
            data005.BP_M = data_form005.cleaned_data['BP_M']
            data005.BP_F = data_form005.cleaned_data['BP_F']
            data005.M_Diaherroea = data_form005.cleaned_data['M_Diaherroea']
            data005.F_Diaherroea = data_form005.cleaned_data['F_Diaherroea']
            data005.M_RTI = data_form005.cleaned_data['M_RTI']
            data005.F_RTI = data_form005.cleaned_data['F_RTI']
            data005.M_Anemia = data_form005.cleaned_data['M_Anemia']
            data005.F_Anemia = data_form005.cleaned_data['F_Anemia']
            data005.worms_Infected_M = data_form005.cleaned_data['worms_Infected_M']
            data005.worms_Infected_F = data_form005.cleaned_data['worms_Infected_F']
            data005.Emotional_Behavivour_M = data_form005.cleaned_data['Emotional_Behavivour_M']
            data005.Emotional_Behavivour_F = data_form005.cleaned_data['Emotional_Behavivour_F']
            data005.save()
            print('Page validated and saved')
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/prs/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/swdd/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    if (current_user.profile.user_lang == 0):
        return render(request, 'data/05msc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/05mscm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
  


def prs_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q006").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D006.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form006 = F006(request.POST)
        data006 = D006()
        print(request.POST)

        if data_form006.is_valid():
            data006.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data006.Preg_Reg_in_Time_G = data_form006.cleaned_data['Preg_Reg_in_Time_G']
            data006.Preg_Reg_in_Time_SC = data_form006.cleaned_data['Preg_Reg_in_Time_SC']
            data006.Preg_Reg_in_Time_ST = data_form006.cleaned_data['Preg_Reg_in_Time_ST']
            data006.Preg_Reg_not_Time_G = data_form006.cleaned_data['Preg_Reg_not_Time_G']
            data006.Preg_Reg_not_Time_SC = data_form006.cleaned_data['Preg_Reg_not_Time_SC']
            data006.Preg_Reg_not_Time_ST = data_form006.cleaned_data['Preg_Reg_not_Time_ST']
            data006.JSSY_JSSK_G = data_form006.cleaned_data['JSSY_JSSK_G']
            data006.JSSY_JSSK_SC = data_form006.cleaned_data['JSSY_JSSK_SC']
            data006.JSSY_JSSK_ST = data_form006.cleaned_data['JSSY_JSSK_ST']
            data006.Birth_Reg_in_Time_G = data_form006.cleaned_data['Birth_Reg_in_Time_G']
            data006.Birth_Reg_in_Time_SC = data_form006.cleaned_data['Birth_Reg_in_Time_SC']
            data006.Birth_Reg_in_Time_ST = data_form006.cleaned_data['Birth_Reg_in_Time_ST']
            data006.EBF_Mothers_G = data_form006.cleaned_data['EBF_Mothers_G']
            data006.EBF_Mothers_SC = data_form006.cleaned_data['EBF_Mothers_SC']
            data006.EBF_Mothers_ST = data_form006.cleaned_data['EBF_Mothers_ST']
            data006.IFA_Tablet_G = data_form006.cleaned_data['IFA_Tablet_G']
            data006.IFA_Tablet_SC = data_form006.cleaned_data['IFA_Tablet_SC']
            data006.IFA_Tablet_ST = data_form006.cleaned_data['IFA_Tablet_ST']
            data006.Risk_Preg_G = data_form006.cleaned_data['Risk_Preg_G']
            data006.Risk_Preg_SC = data_form006.cleaned_data['Risk_Preg_SC']
            data006.Risk_Preg_ST = data_form006.cleaned_data['Risk_Preg_ST']
            data006.Still_Birth_G = data_form006.cleaned_data['Still_Birth_G']
            data006.Still_Birth_SC = data_form006.cleaned_data['Still_Birth_SC']
            data006.Still_Birth_ST = data_form006.cleaned_data['Still_Birth_ST']
            data006.Twins_G = data_form006.cleaned_data['Twins_G']
            data006.Twins_SC = data_form006.cleaned_data['Twins_SC']
            data006.Twins_ST = data_form006.cleaned_data['Twins_ST']
            data006.Institu_Delivery_G = data_form006.cleaned_data['Institu_Delivery_G']
            data006.Institu_Delivery_SC = data_form006.cleaned_data['Institu_Delivery_SC']
            data006.Institu_Delivery_ST = data_form006.cleaned_data['Institu_Delivery_ST']
            data006.Comple_Maternal_Health_Checkup_G = data_form006.cleaned_data['Comple_Maternal_Health_Checkup_G']
            data006.Comple_Maternal_Health_Checkup_SC = data_form006.cleaned_data['Comple_Maternal_Health_Checkup_SC']
            data006.Comple_Maternal_Health_Checkup_ST = data_form006.cleaned_data['Comple_Maternal_Health_Checkup_ST']
            data006.Women_SNP_G = data_form006.cleaned_data['Women_SNP_G']
            data006.Women_SNP_SC = data_form006.cleaned_data['Women_SNP_SC']
            data006.Women_SNP_ST = data_form006.cleaned_data['Women_SNP_ST']
            data006.Maternal_Death_G = data_form006.cleaned_data['Maternal_Death_G']
            data006.Maternal_Death_SC = data_form006.cleaned_data['Maternal_Death_SC']
            data006.Maternal_Death_ST = data_form006.cleaned_data['Maternal_Death_ST']
            data006.MTP_Abortion_G = data_form006.cleaned_data['MTP_Abortion_G']
            data006.MTP_Abortion_SC = data_form006.cleaned_data['MTP_Abortion_SC']
            data006.MTP_Abortion_ST = data_form006.cleaned_data['MTP_Abortion_ST']
            data006.Couples_Without_Children_G = data_form006.cleaned_data['Couples_Without_Children_G']
            data006.Couples_Without_Children_SC = data_form006.cleaned_data['Couples_Without_Children_SC']
            data006.Couples_Without_Children_ST = data_form006.cleaned_data['Couples_Without_Children_ST']
            data006.save()
            print('Page D006 validated and saved')
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/bdr/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/msc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/06prs.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/06prsm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
  


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D007                                                            #
########################################################################################################################################################
def bdr_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q007").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D007.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form007 = F007(request.POST)
        data007 = D007()
        print(request.POST)

        if data_form007.is_valid():
            data007.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data007.S_7_Live_Birth_G = data_form007.cleaned_data['S_7_Live_Birth_G']
            data007.S_7_Live_Birth_SC = data_form007.cleaned_data['S_7_Live_Birth_SC']
            data007.S_7_Live_Birth_ST = data_form007.cleaned_data['S_7_Live_Birth_ST']
            data007.S_7_Neonatal_Death_0_28day_G = data_form007.cleaned_data['S_7_Neonatal_Death_0_28day_G']
            data007.S_7_Neonatal_Death_0_28day_SC = data_form007.cleaned_data['S_7_Neonatal_Death_0_28day_SC']
            data007.S_7_Neonatal_Death_0_28day_ST = data_form007.cleaned_data['S_7_Neonatal_Death_0_28day_ST']
            data007.S_7_Infant_Mortality_0_1_G = data_form007.cleaned_data['S_7_Infant_Mortality_0_1_G']
            data007.S_7_Infant_Mortality_0_1_SC = data_form007.cleaned_data['S_7_Infant_Mortality_0_1_SC']
            data007.S_7_Infant_Mortality_0_1_ST = data_form007.cleaned_data['S_7_Infant_Mortality_0_1_ST']
            data007.S_7_Child_Mortality_1_5_G = data_form007.cleaned_data['S_7_Child_Mortality_1_5_G']
            data007.S_7_Child_Mortality_1_5_SC = data_form007.cleaned_data['S_7_Child_Mortality_1_5_SC']
            data007.S_7_Child_Mortality_1_5_ST = data_form007.cleaned_data['S_7_Child_Mortality_1_5_ST']
            data007.S_7_Death_5_14_Year_G = data_form007.cleaned_data['S_7_Death_5_14_Year_G']
            data007.S_7_Death_5_14_Year_SC = data_form007.cleaned_data['S_7_Death_5_14_Year_SC']
            data007.S_7_Death_5_14_Year_ST = data_form007.cleaned_data['S_7_Death_5_14_Year_ST']
            data007.S_7_Death_Above_14_Year_G = data_form007.cleaned_data['S_7_Death_Above_14_Year_G']
            data007.S_7_Death_Above_14_Year_SC = data_form007.cleaned_data['S_7_Death_Above_14_Year_SC']
            data007.S_7_Death_Above_14_Year_ST = data_form007.cleaned_data['S_7_Death_Above_14_Year_ST']
            data007.S_7_Commited_Suicide_G = data_form007.cleaned_data['S_7_Commited_Suicide_G']
            data007.S_7_Commited_Suicide_SC = data_form007.cleaned_data['S_7_Commited_Suicide_SC']
            data007.S_7_Commited_Suicide_ST = data_form007.cleaned_data['S_7_Commited_Suicide_ST']
            data007.save()
        
            print("Form Seven Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/nhs/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/prs/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/bdr.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/bdrm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
  
  # Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D007                                                            #
########################################################################################################################################################
def nhs_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q008").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D008.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form008 = F008(request.POST)
        data008 = D008()
        print(request.POST)

        if data_form008.is_valid():
            data008.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data008.Newborn_measured = data_form008.cleaned_data['Newborn_measured']
            data008.Newborn_Normal = data_form008.cleaned_data['Newborn_Normal']
            data008.Newborn_Mild = data_form008.cleaned_data['Newborn_Mild']
            data008.Newborn_Moderate = data_form008.cleaned_data['Newborn_Moderate']
            data008.Newborn_Severe = data_form008.cleaned_data['Newborn_Severe']
            data008.Under3_measured = data_form008.cleaned_data['Under3_measured']
            data008.Under3_Normal = data_form008.cleaned_data['Under3_Normal']
            data008.Under3_Mild = data_form008.cleaned_data['Under3_Mild']
            data008.Under3_Moderate = data_form008.cleaned_data['Under3_Moderate']
            data008.Under3_Severe = data_form008.cleaned_data['Under3_Severe']
            data008.Three_5_measured = data_form008.cleaned_data['Three_5_measured']
            data008.Three_5_Normal = data_form008.cleaned_data['Three_5_Normal']
            data008.Three_5_Mild = data_form008.cleaned_data['Three_5_Mild']
            data008.Three_5_Moderate = data_form008.cleaned_data['Three_5_Moderate']
            data008.Three_5_Severe = data_form008.cleaned_data['Three_5_Severe']
            data008.Adolescent_measured = data_form008.cleaned_data['Adolescent_measured']
            data008.Adolescent_Normal = data_form008.cleaned_data['Adolescent_Normal']
            data008.Adolescent_Mild = data_form008.cleaned_data['Adolescent_Mild']
            data008.Adolescent_Moderate = data_form008.cleaned_data['Adolescent_Moderate']
            data008.Adolescent_Severe = data_form008.cleaned_data['Adolescent_Severe']
            data008.Pregnant_measured = data_form008.cleaned_data['Pregnant_measured']
            data008.Pregnant_Normal = data_form008.cleaned_data['Pregnant_Normal']
            data008.Pregnant_Mild = data_form008.cleaned_data['Pregnant_Mild']
            data008.Pregnant_Moderate = data_form008.cleaned_data['Pregnant_Moderate']
            data008.Pregnant_Severe = data_form008.cleaned_data['Pregnant_Severe']

            data008.save()
        
            print("Form Eight Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/ecce/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/bdr/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/nhs.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/nhsm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})

   # Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D009                                                            #
########################################################################################################################################################
def ecce_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q009").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D009.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form009 = F009(request.POST)
        data009 = D009()
        print(request.POST)

        if data_form009.is_valid():
            data009.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data009.Enrolled_AW_SNP = data_form009.cleaned_data['Enrolled_AW_SNP']
            data009.Entolled_Pre_school_AW = data_form009.cleaned_data['Entolled_Pre_school_AW']
            data009.AW_Nutrition_3_5 = data_form009.cleaned_data['AW_Nutrition_3_5']
            data009.Enrolled_other_PreSchool = data_form009.cleaned_data['Enrolled_other_PreSchool']
            data009.AW_Count = data_form009.cleaned_data['AW_Count']
            data009.AW_Own_Bldg = data_form009.cleaned_data['AW_Own_Bldg']
            data009.AW_Temp_Bldg = data_form009.cleaned_data['AW_Temp_Bldg']
            data009.AW_Toilet = data_form009.cleaned_data['AW_Toilet']
            data009.AW_Drinking_Water = data_form009.cleaned_data['AW_Drinking_Water']
            data009.AW_Compound_Wall = data_form009.cleaned_data['AW_Compound_Wall']
            data009.AW_Management_Committee = data_form009.cleaned_data['AW_Management_Committee']
            data009.AW_YoungMothers_Club = data_form009.cleaned_data['AW_YoungMothers_Club']
            data009.AW_With_CP = data_form009.cleaned_data['AW_With_CP']
            data009.save()
        
            print("Form nine Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/ioe/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/nhs/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/09ecce.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/09eccem.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
   

# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D010                                                           #
########################################################################################################################################################
def ioe_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q010").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D010.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form010 = F010(request.POST)
        data010 = D010()
        print(request.POST)

        if data_form010.is_valid():   
	        data010.lsgd_code_and_year = lsgd_code + str(data_entry_year)
	        data010.LP_School_Govt = data_form010.cleaned_data['LP_School_Govt']
	        data010.LP_School_LSG = data_form010.cleaned_data['LP_School_LSG']
	        data010.LP_School_Aided = data_form010.cleaned_data['LP_School_Aided']
	        data010.LP_School_Un_Aided = data_form010.cleaned_data['LP_School_Un_Aided']
	        data010.UP_School_Govt = data_form010.cleaned_data['UP_School_Govt']
	        data010.UP_School_LSG = data_form010.cleaned_data['UP_School_LSG']
	        data010.UP_School_Aided = data_form010.cleaned_data['UP_School_Aided']
	        data010.UP_School_Un_Aided = data_form010.cleaned_data['UP_School_Un_Aided']
	        data010.High_School_Govt = data_form010.cleaned_data['High_School_Govt']
	        data010.High_School_LSG = data_form010.cleaned_data['High_School_LSG']
	        data010.High_School_Aided = data_form010.cleaned_data['High_School_Aided']
	        data010.High_School_Un_Aided = data_form010.cleaned_data['High_School_Un_Aided']
	        data010.Higher_Secondary_Govt = data_form010.cleaned_data['Higher_Secondary_Govt']
	        data010.Higher_Secondary_LSG = data_form010.cleaned_data['Higher_Secondary_LSG']
	        data010.Higher_Secondary_Aided = data_form010.cleaned_data['Higher_Secondary_Aided']
	        data010.Higher_Secondary_Un_Aided = data_form010.cleaned_data['Higher_Secondary_Un_Aided']
	        data010.Vocational_Higher_Secondary_Govt = data_form010.cleaned_data['Vocational_Higher_Secondary_Govt']
	        data010.Vocational_Higher_Secondary_LSG = data_form010.cleaned_data['Vocational_Higher_Secondary_LSG']
	        data010.Vocational_Higher_Secondary_Aided = data_form010.cleaned_data['Vocational_Higher_Secondary_Aided']
	        data010.Vocational_Higher_Secondary_Un_Aided = data_form010.cleaned_data['Vocational_Higher_Secondary_Un_Aided']
	        data010.Open_School_Centers_Govt = data_form010.cleaned_data['Open_School_Centers_Govt']
	        data010.Open_School_Centers_LSG = data_form010.cleaned_data['Open_School_Centers_LSG']
	        data010.Open_School_Centers_Aided = data_form010.cleaned_data['Open_School_Centers_Aided']
	        data010.Open_School_Centers_Un_Aided = data_form010.cleaned_data['Open_School_Centers_Un_Aided']
	        data010.Anganwadi_Centers_Govt = data_form010.cleaned_data['Anganwadi_Centers_Govt']
	        data010.Anganwadi_Centers_LSG = data_form010.cleaned_data['Anganwadi_Centers_LSG']
	        data010.Anganwadi_Centers_Aided = data_form010.cleaned_data['Anganwadi_Centers_Aided']
	        data010.Anganwadi_Centers_Un_Aided = data_form010.cleaned_data['Anganwadi_Centers_Un_Aided']
	        data010.Nursery_Pre_Primary_Govt = data_form010.cleaned_data['Nursery_Pre_Primary_Govt']
	        data010.Nursery_Pre_Primary_LSG = data_form010.cleaned_data['Nursery_Pre_Primary_LSG']
	        data010.Nursery_Pre_Primary_Aided = data_form010.cleaned_data['Nursery_Pre_Primary_Aided']
	        data010.Nursery_Pre_Primary_Un_Aided = data_form010.cleaned_data['Nursery_Pre_Primary_Un_Aided']
	        data010.save()
            #print("Form ten Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/sddosc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/ecce/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
        
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/10ioe.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/10ioem.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    

# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D011                                                           #
########################################################################################################################################################
def sddosc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q011").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D011.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form011 = F011(request.POST)
        data011 = D011()
        print(request.POST)

        if data_form011.is_valid():
            data011.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data011.Total_NoofSchool = data_form011.cleaned_data['Total_NoofSchool']
            data011.Total_Students_M = data_form011.cleaned_data['Total_Students_M']
            data011.Total_Students_F = data_form011.cleaned_data['Total_Students_F']
            data011.Total_Student_Transfered_Out = data_form011.cleaned_data['Total_Student_Transfered_Out']
            data011.Total_Students_Dropout = data_form011.cleaned_data['Total_Students_Dropout']
            data011.Total_Chronic_Absentees = data_form011.cleaned_data['Total_Chronic_Absentees']
            data011.Total_Dropout_SCST = data_form011.cleaned_data['Total_Dropout_SCST']
            data011.Total_CWSN = data_form011.cleaned_data['Total_CWSN']
            data011.Total_Children_LD = data_form011.cleaned_data['Total_Children_LD']
            data011.Total_CWD = data_form011.cleaned_data['Total_CWD']
            data011.save()
            #print("Form eleven Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/icos/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/ioe/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/11sddosc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/11sddoscm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
 


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D012                                                           #
########################################################################################################################################################
def icos_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q012").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D012.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form012 = F012(request.POST)
        data012 = D012()
        print(request.POST)

        if data_form012.is_valid():
            data012.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data012.No_of_School = data_form012.cleaned_data['No_of_School']
            data012.Buiding_Permanent = data_form012.cleaned_data['Buiding_Permanent']
            data012.Buiding_Temperory = data_form012.cleaned_data['Buiding_Temperory']
            data012.Smart_Class_Room = data_form012.cleaned_data['Smart_Class_Room']
            data012.Barrier_Free_Status = data_form012.cleaned_data['Barrier_Free_Status']
            data012.Drinking_Water = data_form012.cleaned_data['Drinking_Water']
            data012.Toilets = data_form012.cleaned_data['Toilets']
            data012.Waste_Disposal_Facility = data_form012.cleaned_data['Waste_Disposal_Facility']
            data012.Play_Ground_with_STD = data_form012.cleaned_data['Play_Ground_with_STD']
            data012.Kitchen_Permanent = data_form012.cleaned_data['Kitchen_Permanent']
            data012.Kitchen_Temperory = data_form012.cleaned_data['Kitchen_Temperory']
            data012.School_With_Green_Initative = data_form012.cleaned_data['School_With_Green_Initative']
            data012.save()
            print("Form twelve Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/hci/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/sddosc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/12icos.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/12icosm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
 



# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D013                                                          #
########################################################################################################################################################
def hci_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]

    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q013").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D013.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form013 = F013(request.POST)
        data013 = D013()
        print(request.POST)

        if data_form013.is_valid():
            data013.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data013.PHC_Govt = data_form013.cleaned_data['PHC_Govt']
            data013.PHC_Private = data_form013.cleaned_data['PHC_Private']
            data013.PHC_OP = data_form013.cleaned_data['PHC_OP']
            data013.PHC_IP = data_form013.cleaned_data['PHC_IP']
            data013.PHC_Labour = data_form013.cleaned_data['PHC_Labour']
            data013.PHC_Infant_Treatment = data_form013.cleaned_data['PHC_Infant_Treatment']
            data013.PHC_Operation = data_form013.cleaned_data['PHC_Operation']
            data013.Dispensary_Govt = data_form013.cleaned_data['Dispensary_Govt']
            data013.Dispensary_Private = data_form013.cleaned_data['Dispensary_Private']
            data013.Dispensary_OP = data_form013.cleaned_data['Dispensary_OP']
            data013.Dispensary_IP = data_form013.cleaned_data['Dispensary_IP']
            data013.Dispensary_Labour = data_form013.cleaned_data['Dispensary_Labour']
            data013.Dispensary_Infant_Treatment = data_form013.cleaned_data['Dispensary_Infant_Treatment']
            data013.Dispensary_Operation = data_form013.cleaned_data['Dispensary_Operation']
            data013.Hospital_Govt = data_form013.cleaned_data['Hospital_Govt']
            data013.Hospital_Private = data_form013.cleaned_data['Hospital_Private']
            data013.Hospital_OP = data_form013.cleaned_data['Hospital_OP']
            data013.Hospital_IP = data_form013.cleaned_data['Hospital_IP']
            data013.Hospital_Labour = data_form013.cleaned_data['Hospital_Labour']
            data013.Hospital_Infant_Treatment = data_form013.cleaned_data['Hospital_Infant_Treatment']
            data013.Hospital_Operation = data_form013.cleaned_data['Hospital_Operation']
            data013.Jilla_Hospital_Govt = data_form013.cleaned_data['Jilla_Hospital_Govt']
            data013.Jilla_Hospital_Private = data_form013.cleaned_data['Jilla_Hospital_Private']
            data013.Jilla_Hospital_OP = data_form013.cleaned_data['Jilla_Hospital_OP']
            data013.Jilla_Hospital_IP = data_form013.cleaned_data['Jilla_Hospital_IP']
            data013.Jilla_Hospital_Labour = data_form013.cleaned_data['Jilla_Hospital_Labour']
            data013.Jilla_Hospital_Infant_Treatment = data_form013.cleaned_data['Jilla_Hospital_Infant_Treatment']
            data013.Jilla_Hospital_Operation = data_form013.cleaned_data['Jilla_Hospital_Operation']
            data013.General_Hospital_Govt = data_form013.cleaned_data['General_Hospital_Govt']
            data013.General_Hospital_Private = data_form013.cleaned_data['General_Hospital_Private']
            data013.General_Hospital_OP = data_form013.cleaned_data['General_Hospital_OP']
            data013.General_Hospital_IP = data_form013.cleaned_data['General_Hospital_IP']
            data013.General_Hospital_Labour = data_form013.cleaned_data['General_Hospital_Labour']
            data013.General_Hospital_Infant_Treatment = data_form013.cleaned_data['General_Hospital_Infant_Treatment']
            data013.General_Hospital_Operation = data_form013.cleaned_data['General_Hospital_Operation']
            data013.Alopathy_Clinic_Govt = data_form013.cleaned_data['Alopathy_Clinic_Govt']
            data013.Alopathy_Clinic_Private = data_form013.cleaned_data['Alopathy_Clinic_Private']
            data013.Alopathy_Clinic_OP = data_form013.cleaned_data['Alopathy_Clinic_OP']
            data013.Alopathy_Clinic_IP = data_form013.cleaned_data['Alopathy_Clinic_IP']
            data013.Alopathy_Clinic_Labour = data_form013.cleaned_data['Alopathy_Clinic_Labour']
            data013.Alopathy_Clinic_Infant_Treatment = data_form013.cleaned_data['Alopathy_Clinic_Infant_Treatment']
            data013.Alopathy_Clinic_Operation = data_form013.cleaned_data['Alopathy_Clinic_Operation']
            data013.Ayurvedam_Govt = data_form013.cleaned_data['Ayurvedam_Govt']
            data013.Ayurvedam_Private = data_form013.cleaned_data['Ayurvedam_Private']
            data013.Ayurvedam_OP = data_form013.cleaned_data['Ayurvedam_OP']
            data013.Ayurvedam_IP = data_form013.cleaned_data['Ayurvedam_IP']
            data013.Ayurvedam_Labour = data_form013.cleaned_data['Ayurvedam_Labour']
            data013.Ayurvedam_Infant_Treatment = data_form013.cleaned_data['Ayurvedam_Infant_Treatment']
            data013.Ayurvedam_Operation = data_form013.cleaned_data['Ayurvedam_Operation']
            data013.Homeo_Govt = data_form013.cleaned_data['Homeo_Govt']
            data013.Homeo_Private = data_form013.cleaned_data['Homeo_Private']
            data013.Homeo_OP = data_form013.cleaned_data['Homeo_OP']
            data013.Homeo_IP = data_form013.cleaned_data['Homeo_IP']
            data013.Homeo_Labour = data_form013.cleaned_data['Homeo_Labour']
            data013.Homeo_Infant_Treatment = data_form013.cleaned_data['Homeo_Infant_Treatment']
            data013.Homeo_Operation = data_form013.cleaned_data['Homeo_Operation']
            data013.Other_Ayush_Centers_Govt = data_form013.cleaned_data['Other_Ayush_Centers_Govt']
            data013.Other_Ayush_Centers_Private = data_form013.cleaned_data['Other_Ayush_Centers_Private']
            data013.Other_Ayush_Centers_OP = data_form013.cleaned_data['Other_Ayush_Centers_OP']
            data013.Other_Ayush_Centers_IP = data_form013.cleaned_data['Other_Ayush_Centers_IP']
            data013.Other_Ayush_Centers_Labour = data_form013.cleaned_data['Other_Ayush_Centers_Labour']
            data013.Other_Ayush_Centers_Infant_Treatment = data_form013.cleaned_data['Other_Ayush_Centers_Infant_Treatment']
            data013.Other_Ayush_Centers_Operation = data_form013.cleaned_data['Other_Ayush_Centers_Operation']
            data013.MCH_Govt = data_form013.cleaned_data['MCH_Govt']
            data013.MCH_Private = data_form013.cleaned_data['MCH_Private']
            data013.MCH_OP = data_form013.cleaned_data['MCH_OP']
            data013.MCH_IP = data_form013.cleaned_data['MCH_IP']
            data013.MCH_Labour = data_form013.cleaned_data['MCH_Labour']
            data013.MCH_Infant_Treatment = data_form013.cleaned_data['MCH_Infant_Treatment']
            data013.MCH_Operation = data_form013.cleaned_data['MCH_Operation']
            data013.save()
            #print("Form thirteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/oifc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/icos/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/13hci.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/13hcim.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
 

# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D014                                                          #
########################################################################################################################################################
def oifc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]

    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q014").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D014.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form014 = F014(request.POST)
        data014 = D014()
        print(request.POST)

        if data_form014.is_valid():
            data014.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data014.Disability_Management_Institution = data_form014.cleaned_data['Disability_Management_Institution']
            data014.Disability_Management_Govt = data_form014.cleaned_data['Disability_Management_Govt']
            data014.Disability_Management_LSG = data_form014.cleaned_data['Disability_Management_LSG']
            data014.Disability_Management_NGO = data_form014.cleaned_data['Disability_Management_NGO']
            data014.Disability_Management_Private = data_form014.cleaned_data['Disability_Management_Private']
            data014.Mental_Health_Institution = data_form014.cleaned_data['Mental_Health_Institution']
            data014.Mental_Health_Govt = data_form014.cleaned_data['Mental_Health_Govt']
            data014.Mental_Health_LSG = data_form014.cleaned_data['Mental_Health_LSG']
            data014.Mental_Health_NGO = data_form014.cleaned_data['Mental_Health_NGO']
            data014.Mental_Health_Private = data_form014.cleaned_data['Mental_Health_Private']
            data014.Special_Education_Institution = data_form014.cleaned_data['Special_Education_Institution']
            data014.Special_Education_Govt = data_form014.cleaned_data['Special_Education_Govt']
            data014.Special_Education_LSG = data_form014.cleaned_data['Special_Education_LSG']
            data014.Special_Education_NGO = data_form014.cleaned_data['Special_Education_NGO']
            data014.Special_Education_Private = data_form014.cleaned_data['Special_Education_Private']
            data014.Institutional_Care_Institution = data_form014.cleaned_data['Institutional_Care_Institution']
            data014.Institutional_Care_Govt = data_form014.cleaned_data['Institutional_Care_Govt']
            data014.Institutional_Care_LSG = data_form014.cleaned_data['Institutional_Care_LSG']
            data014.Institutional_Care_NGO = data_form014.cleaned_data['Institutional_Care_NGO']
            data014.Institutional_Care_Private = data_form014.cleaned_data['Institutional_Care_Private']
            data014.Protection_Services_Institution = data_form014.cleaned_data['Protection_Services_Institution']
            data014.Protection_Services_Govt = data_form014.cleaned_data['Protection_Services_Govt']
            data014.Protection_Services_LSG = data_form014.cleaned_data['Protection_Services_LSG']
            data014.Protection_Services_NGO = data_form014.cleaned_data['Protection_Services_NGO']
            data014.Protection_Services_Private = data_form014.cleaned_data['Protection_Services_Private']
            data014.Scanning_Centre_Institution = data_form014.cleaned_data['Scanning_Centre_Institution']
            data014.Scanning_Centre_Govt = data_form014.cleaned_data['Scanning_Centre_Govt']
            data014.Scanning_Centre_LSG = data_form014.cleaned_data['Scanning_Centre_LSG']
            data014.Scanning_Centre_NGO = data_form014.cleaned_data['Scanning_Centre_NGO']
            data014.Scanning_Centre_Private = data_form014.cleaned_data['Scanning_Centre_Private']
            data014.Theraphy_Centre_Institution = data_form014.cleaned_data['Theraphy_Centre_Institution']
            data014.Theraphy_Centre_Govt = data_form014.cleaned_data['Theraphy_Centre_Govt']
            data014.Theraphy_Centre_LSG = data_form014.cleaned_data['Theraphy_Centre_LSG']
            data014.Theraphy_Centre_NGO = data_form014.cleaned_data['Theraphy_Centre_NGO']
            data014.Theraphy_Centre_Private = data_form014.cleaned_data['Theraphy_Centre_Private']
            data014.Palliataive_Care_Institution = data_form014.cleaned_data['Palliataive_Care_Institution']
            data014.Palliataive_Care_Govt = data_form014.cleaned_data['Palliataive_Care_Govt']
            data014.Palliataive_Care_LSG = data_form014.cleaned_data['Palliataive_Care_LSG']
            data014.Palliataive_Care_NGO = data_form014.cleaned_data['Palliataive_Care_NGO']
            data014.Palliataive_Care_Private = data_form014.cleaned_data['Palliataive_Care_Private']
            data014.Clinical_Lab_Institution = data_form014.cleaned_data['Clinical_Lab_Institution']
            data014.Clinical_Lab_Govt = data_form014.cleaned_data['Clinical_Lab_Govt']
            data014.Clinical_Lab_LSG = data_form014.cleaned_data['Clinical_Lab_LSG']
            data014.Clinical_Lab_NGO = data_form014.cleaned_data['Clinical_Lab_NGO']
            data014.Clinical_Lab_Private = data_form014.cleaned_data['Clinical_Lab_Private']
            data014.Deaddition_Centres_Institution = data_form014.cleaned_data['Deaddition_Centres_Institution']
            data014.Deaddition_Centres_Govt = data_form014.cleaned_data['Deaddition_Centres_Govt']
            data014.Deaddition_Centres_LSG = data_form014.cleaned_data['Deaddition_Centres_LSG']
            data014.Deaddition_Centres_NGO = data_form014.cleaned_data['Deaddition_Centres_NGO']
            data014.Deaddition_Centres_Private = data_form014.cleaned_data['Deaddition_Centres_Private']
            data014.save()
            print("Form forteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/icop/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/hci/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/14oifc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/14oifcm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})




# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D015                                                           #
########################################################################################################################################################

def icop_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q015").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D015.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form015 = F015(request.POST)
        data015 = D015()
        print(request.POST)

        if data_form015.is_valid():
            data015.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data015.No_of_SC_Household = data_form015.cleaned_data['No_of_SC_Household']
            data015.No_of_ST_Household = data_form015.cleaned_data['No_of_ST_Household']
            data015.Ashraya_Family = data_form015.cleaned_data['Ashraya_Family']
            data015.Single_Room_Household = data_form015.cleaned_data['Single_Room_Household']
            data015.Un_Electrified_Household = data_form015.cleaned_data['Un_Electrified_Household']
            data015.Household_Without_DrinkingWater = data_form015.cleaned_data['Household_Without_DrinkingWater']
            data015.Household_Without_Toilet = data_form015.cleaned_data['Household_Without_Toilet']
            data015.Public_Place_Without_Waste_Disposal = data_form015.cleaned_data['Public_Place_Without_Waste_Disposal']
            data015.Homless_Family = data_form015.cleaned_data['Homless_Family']
            data015.Children_Exposed_to_Abuse = data_form015.cleaned_data['Children_Exposed_to_Abuse']
            data015.save()
            #print("Form fifteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/cetv/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/oifc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/15icop.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/15icopm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})




# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D011                                                           #
########################################################################################################################################################
def cetv_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q016").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D016.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form016 = F016(request.POST)
        data016 = D016()
        print(request.POST)

        if data_form016.is_valid():
            data016.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data016.Under_Orphanges = data_form016.cleaned_data['Under_Orphanges']
            data016.Under_Premetric_Hostel = data_form016.cleaned_data['Under_Premetric_Hostel']
            data016.Missing = data_form016.cleaned_data['Missing']
            data016.Conflict_with_Law = data_form016.cleaned_data['Conflict_with_Law']
            data016.Children_Under_CWC = data_form016.cleaned_data['Children_Under_CWC']
            data016.POCSO_Cases = data_form016.cleaned_data['POCSO_Cases']
            data016.At_Risk = data_form016.cleaned_data['At_Risk']
            data016.Adopted = data_form016.cleaned_data['Adopted']
            data016.Foster_Care_Sponsorship = data_form016.cleaned_data['Foster_Care_Sponsorship']
            data016.Road_Accidents = data_form016.cleaned_data['Road_Accidents']
            data016.Calamities = data_form016.cleaned_data['Calamities']
            data016.Orphant_Children = data_form016.cleaned_data['Orphant_Children']
            data016.HIV_Effected_Family = data_form016.cleaned_data['HIV_Effected_Family']
            data016.Migrant_Labours = data_form016.cleaned_data['Migrant_Labours']
            data016.Diability = data_form016.cleaned_data['Diability']
            data016.Bedridden = data_form016.cleaned_data['Bedridden']
            data016.Child_Labour = data_form016.cleaned_data['Child_Labour']
            data016.Child_Marriage = data_form016.cleaned_data['Child_Marriage']
            data016.UnWed_Mothers = data_form016.cleaned_data['UnWed_Mothers']
            data016.Physical_Punishment = data_form016.cleaned_data['Physical_Punishment']
            data016.save()
            #print("Form sixteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/cp/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/icop/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/16cetv.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/16cetvm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})



# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D017                                                          #
########################################################################################################################################################
def cp_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q017").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D017.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form017 = F017(request.POST)
        data017 = D017()
        print(request.POST)

        if data_form017.is_valid():
            data017.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data017.Balasabha = data_form017.cleaned_data['Balasabha']
            data017.Bala_Panchayat = data_form017.cleaned_data['Bala_Panchayat']
            data017.AG_Club = data_form017.cleaned_data['AG_Club']
            data017.AB_Club = data_form017.cleaned_data['AB_Club']
            data017.Children_Gramasabha = data_form017.cleaned_data['Children_Gramasabha']
            data017.Working_Group = data_form017.cleaned_data['Working_Group']
            data017.School_Club = data_form017.cleaned_data['School_Club']
            data017.Vigilance_Committee = data_form017.cleaned_data['Vigilance_Committee']
            data017.Social_Audit = data_form017.cleaned_data['Social_Audit']
            data017.save()
            #print("Form seventeen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/lcc/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/cetv/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    if (current_user.profile.user_lang == 0):
        return render(request, 'data/17cp.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/17cpm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D018                                                          #
########################################################################################################################################################
def lcc_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q018").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D018.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form018 = F018(request.POST)
        data018 = D018()
        print(request.POST)

        if data_form018.is_valid():
            data018.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data018.Public_Library = data_form018.cleaned_data['Public_Library']
            data018.Children_Library = data_form018.cleaned_data['Children_Library']
            data018.AG_Club_at_AWC = data_form018.cleaned_data['AG_Club_at_AWC']
            data018.Sports_Arts_Club = data_form018.cleaned_data['Sports_Arts_Club']
            data018.Cinema_Theatre = data_form018.cleaned_data['Cinema_Theatre']
            data018.Cultural_Sports_Centre = data_form018.cleaned_data['Cultural_Sports_Centre']
            data018.Community_Hall = data_form018.cleaned_data['Community_Hall']
            data018.Children_Park = data_form018.cleaned_data['Children_Park']
            data018.Play_Ground = data_form018.cleaned_data['Play_Ground']
            data018.Stadium = data_form018.cleaned_data['Stadium']
            data018.Swimming_Pool = data_form018.cleaned_data['Swimming_Pool']
            data018.save()
            #print("Form eighteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/cfai/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/cp/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")
    
    if (current_user.profile.user_lang == 0):
        return render(request, 'data/18lcc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/18lccm.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D018                                                          #
########################################################################################################################################################
def cfai_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]

    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q019").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D019.objects.filter(lsgd_code_and_year = reqd_data )
    
    if request.method == 'POST':
        data_form019 = F019(request.POST)
        data019 = D019()
        print(request.POST)

        if data_form019.is_valid():
            data019.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data019.Zero_Zone = data_form019.cleaned_data['Zero_Zone']
            data019.Zebra_Crossing = data_form019.cleaned_data['Zebra_Crossing']
            data019.School_Accident_Zone = data_form019.cleaned_data['School_Accident_Zone']
            data019.Complaint_Box = data_form019.cleaned_data['Complaint_Box']
            data019.Vigilance_Committee = data_form019.cleaned_data['Vigilance_Committee']
            data019.Child_Friendly_Health_Institution = data_form019.cleaned_data['Child_Friendly_Health_Institution']
            data019.Model_Anganwadi = data_form019.cleaned_data['Model_Anganwadi']
            data019.Jagrathasamithi = data_form019.cleaned_data['Jagrathasamithi']
            data019.Playground_Upgraded = data_form019.cleaned_data['Playground_Upgraded']
            data019.Public_Place_Upgraded = data_form019.cleaned_data['Public_Place_Upgraded']
            data019.S1takeholder_Meeting = data_form019.cleaned_data['Stakeholder_Meeting']
            data019.Public_Private_Coordination = data_form019.cleaned_data['Public_Private_Coordination']
            data019.Hospital_Development_Committee = data_form019.cleaned_data['Hospital_Development_Committee']
            data019.VHNSC = data_form019.cleaned_data['VHNSC']
            data019.VEC = data_form019.cleaned_data['VEC']
            data019.PTA = data_form019.cleaned_data['PTA']
            data019.ICDS_Coordination = data_form019.cleaned_data['ICDS_Coordination']
            data019.SCST_SubCommittee = data_form019.cleaned_data['SCST_SubCommittee']
            data019.IEC_Material_Exbited_Vaccination = data_form019.cleaned_data['IEC_Material_Exbited_Vaccination']
            data019.save()
            #print("Form ninteen Committed")
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/gdls/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/lcc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    if (current_user.profile.user_lang == 0):
        return render(request, 'data/19cfai.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
    else:
        return render(request, 'data/19cfaim.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})
