from django.shortcuts import render, redirect

from dyna.models import Qbank
from data.forms import DataForm01


# Create your views here.
def gdls_page(request):
    Qset = '01'
    
    questions_queryset =  QBank.objects.filter(Qcode = Qset).values()
    
    questions_list = []
    for q in questions_queryset:
        questions_list.append(q['question_text'])

    if request.method == 'POST':
        #return render(request, 'r2n2/index.html')
        data_form01 = DataForm01(request.POST)
        data01 = D01_GeneralDetails()
        if data_form01.is_valid():
            data01.lsgd_code_and_year = lsgd_code + str(data_entry_year)
            data01.lsgd_name = data_form01.cleaned_data['lsgd_name']
            data01.lsgd_year_of_formation = data_form01.cleaned_data['lsgd_year_of_formation']
            data01.lsgd_area_in_sqkm = data_form01.cleaned_data['lsgd_area_in_sqkm']e.
