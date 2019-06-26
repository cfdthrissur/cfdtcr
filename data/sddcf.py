from django.shortcuts import render, redirect
from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd
from data.models import D003
from data.forms import F003

def sddc_compile(request):

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
        
            print(data_form03.cleaned_data['Page validated and saved'])
        else:
            print('Form not valid')    

        if 'next_page' in request.POST:
            print("Next page clicked")
            return redirect('/data/swdd/')
        elif 'prev_page' in request.POST:
            print("Prev page clicked")
            return redirect('/data/sddc/')
        else:
            print("Save details clicked")
          
    else:
        print("Not a POST request")

    return render(request, 'data/sddc.html', {'questions': questions_queryset, 'lsgd_selected': lsgd_selected, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'answers': current_answerset})