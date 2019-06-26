from django.shortcuts import render, redirect
from itertools import chain

from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd, Taluk, Block, Assembly, Parliament
from data.models import D001, D002, D003, D004, D005, D006, D007, D008, D009, D010, D011, D012, D013, D014, D015, D016, D017, D018, D019


# Create your views here.
def view_page(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]

    lsgds = Lsgd.objects.all()
    question_headers = QuestionHeader.objects.all()
    taluks = Taluk.objects.filter(taluk_code__startswith = district_code).values().order_by('taluk_code')
    blocks = Block.objects.filter(block_code__startswith = district_code).values().order_by('block_code')
    assemblys = Assembly.objects.filter(assembly_code__startswith = district_code).values().order_by('assembly_code')
    parliaments = Parliament.objects.filter(parliament_code__startswith = district_code).values().order_by('parliament_code')
    questions_queryset = ""
    current_answerset = ""
    questions_and_answers =[]
    lsgd_selected = lsgd_code
    header_selected = "H001"

    if request.method == 'POST':
        questions_queryset =  QuestionBank.objects.filter(question_code__startswith = "Q"+request.POST.get('question_header')[1:]).values_list('question_text').order_by('question_code')
        questions_queryset = list(chain.from_iterable(questions_queryset))
        lsgd_selected = request.POST.get('lsgd_selected')
        header_selected = request.POST.get('question_header')
        
        ##############################################################################################################
        if header_selected == "H001":
            current_answerset = D001.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H002":
            current_answerset = D002.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H003":
            current_answerset = D003.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H004":
            current_answerset = D004.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H005":
            current_answerset = D005.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H006":
            current_answerset = D006.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H007":
            current_answerset = D007.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H008":
            current_answerset = D008.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H009":
            current_answerset = D009.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H010":
            current_answerset = D010.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H011":
            current_answerset = D011.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H012":
            current_answerset = D012.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()      
        elif header_selected == "H013":
            current_answerset = D013.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H014":
            current_answerset = D014.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H015":
            current_answerset = D015.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H016":
            current_answerset = D016.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        elif header_selected == "H017":
            current_answerset = D017.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list() 
        elif header_selected == "H018":
            current_answerset = D018.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()
        else:
            current_answerset = D019.objects.filter(lsgd_code_and_year = lsgd_selected + str(data_entry_year)).values_list()


        current_answerset = list(chain.from_iterable(current_answerset))[1:]
        questions_and_answers = zip ( questions_queryset, current_answerset)

    return render(request, 'rpts/view.html', {'questions': questions_queryset, 'answers': current_answerset, 'lsgds': lsgds, 'data_entry_year': data_entry_year, 'question_headers': question_headers,\
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments, \
                            'questions_and_answers': questions_and_answers, 'lsgd_selected': lsgd_selected,  'header_selected': header_selected})


def lsgd_page(request):
    lsgds = Lsgd.objects.all()
    return render(request, 'rpts/lsgd.html', {'lsgds': lsgds})

def blck_page(request):
    blocks = Block.objects.all()
    return render(request, 'rpts/blck.html', {'blocks': blocks})

def talk_page(request):
    taluks = Taluk.objects.all()
    return render(request, 'rpts/talk.html', {'taluks': taluks})

def asmb_page(request):
    assemblys = Assembly.objects.all()
    return render(request, 'rpts/asmb.html', {'assemblys': assemblys})

def plmt_page(request):
    parliaments = Parliament.objects.all()
    return render(request, 'rpts/plmt.html', {'parliaments': parliaments})

def sexratio(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]

    lsgds = Lsgd.objects.all()
    question_headers = QuestionHeader.objects.all()
    taluks = Taluk.objects.filter(taluk_code__startswith = district_code).values().order_by('taluk_code')
    blocks = Block.objects.filter(block_code__startswith = district_code).values().order_by('block_code')
    assemblys = Assembly.objects.filter(assembly_code__startswith = district_code).values().order_by('assembly_code')
    parliaments = Parliament.objects.filter(parliament_code__startswith = district_code).values().order_by('parliament_code')
    lsgd_selected = lsgd_code
    reqd_data = lsgd_code + str(data_entry_year)
    current_answerset = D002.objects.filter(lsgd_code_and_year = reqd_data )
    gr = 0
    cr = 0
    dm = 0

    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_answerset = D002.objects.filter(lsgd_code_and_year = reqd_data )
        gm = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("population_male", flat=True)
        gf = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("population_female", flat=True)
        gr = ( gf[0] / gm[0] ) * 1000
        gr = int(gr)
        gm = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("children_0_to_6_age_male", flat=True)
        gf = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("children_0_to_6_age_female", flat=True)
        cr = ( gf[0] / gm[0] ) * 1000
        cr = int(cr)
        dm = D002.objects.all().aggregate(Sum('population_male'))

    
    return render(request, 'analyse/sexratio.html', {'answers': current_answerset, 'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'taluks': taluks, 'blocks': blocks, 'assemblys': assemblys, 'parliaments': parliaments, \
                            'lsgd_selected': lsgd_selected, 'gratio': gr, 'cratio': cr, 'dsr': dm})