from django.shortcuts import render, redirect

from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd, Taluk, Block, Assembly, Parliament
from data.models import D004

from data.forms import F004


# Create your views here.
########################################################################################################################################################
#                                                  Data Entry for D001 - General Details                                                               #
########################################################################################################################################################
def swdd_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]


    questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q004").values().order_by('question_code')
    lsgd_selected = Lsgd.objects.filter(lsgd_code = lsgd_code)
    taluks = Taluk.objects.filter(taluk_code__startswith = district_code).values().order_by('taluk_code')
    blocks = Block.objects.filter(block_code__startswith = district_code).values().order_by('block_code')
    assemblys = Assembly.objects.filter(assembly_code__startswith = district_code).values().order_by('assembly_code')
    parliaments = Parliament.objects.filter(parliament_code__startswith = district_code).values().order_by('parliament_code')


    if request.method == 'POST':
        data_form01 = F004(request.POST)
        data01 = D004()
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
        
            print(data_form01.cleaned_data['lsgd_name'])
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/demp/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    return render(request, 'data/gdls.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments})




