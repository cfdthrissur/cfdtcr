from django.shortcuts import render, redirect
from itertools import chain

from qbnk.models import QuestionBank, QuestionHeader
from lsgd.models import Lsgd, Taluk, Block, Assembly, Parliament
from data.models import D001, D002, D003, D004, D005, D006, D007, D008, D009, D010, D011, D012, D013, D014, D015, D016, D017, D018, D019
from django.db.models import Sum

# Create your views here.

def menu(request):
     return render(request, 'analyse/menu.html', {})

def sexratio(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]
    lsgd_selected = lsgd_code
    current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
    current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
    lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
    lsgd_inblock_year = []
    for x in lsgd_inblock:
        xz = ''.join(x)
        lsgd_inblock_year.append(xz+str(data_entry_year))
    
    lsgds = Lsgd.objects.all()
    blocks = Block.objects.filter(block_code = current_block[0]) 
    reqd_data = lsgd_code + str(data_entry_year)
    
    sexratio = [0,0,0,0,0,0]
    popmale = [0,0,0,0,0,0]
    popfemale = [0,0,0,0,0,0]
       

    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
        current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
        lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
        lsgd_inblock_year = []
        for x in lsgd_inblock:
            xz = ''.join(x)
            lsgd_inblock_year.append(xz+str(data_entry_year))
        
        lsgds = Lsgd.objects.all()
        blocks = Block.objects.filter(block_code = current_block[0]) 
                
        td = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("population_male","population_female" )
        td = list(td[0]) 
        popmale[0]=td[0]
        popfemale[0]=td[1]
        sexratio[0]=int((td[1]/td[0])*1000)

        td = D002.objects.filter(lsgd_code_and_year = reqd_data ).values_list("children_0_to_6_age_male","children_0_to_6_age_female" )
        td = list(td[0])
        popmale[1]=td[0]
        popfemale[1]=td[1]
        sexratio[1]=int((td[1]/td[0])*1000)

        td = D002.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate( Sum("population_male"), Sum("population_female"), Sum("children_0_to_6_age_male"), Sum('children_0_to_6_age_female'))
        popmale[2] = td['population_male__sum']
        popfemale[2]=td['population_female__sum']
        sexratio[2]=int((td['population_female__sum']/td['population_male__sum'])*1000)

        popmale[3]=td['children_0_to_6_age_male__sum']
        popfemale[3]=td['children_0_to_6_age_female__sum']
        sexratio[3]=int((td['children_0_to_6_age_female__sum']/td['children_0_to_6_age_male__sum'])*1000)

        td = D002.objects.aggregate( Sum("population_male"), Sum("population_female"), Sum("children_0_to_6_age_male"), Sum('children_0_to_6_age_female'))
        popmale[4] = td['population_male__sum']
        popfemale[4]=td['population_female__sum']
        sexratio[4]=int((td['population_female__sum']/td['population_male__sum'])*1000)

        popmale[5]=td['children_0_to_6_age_male__sum']
        popfemale[5]=td['children_0_to_6_age_female__sum']
        sexratio[5]=int((td['children_0_to_6_age_female__sum']/td['children_0_to_6_age_male__sum'])*1000)
       
            
    return render(request, 'analyse/sexratio.html', { 'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'current_lsgd': current_name, 'blocks': blocks, \
                            'lsgd_selected': lsgd_selected, 'sexratio': sexratio, 'popmale': popmale, 'popfemale': popfemale })

    
def mortality(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]
    lsgd_selected = lsgd_code
    current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
    current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
    lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
    lsgd_inblock_year = []
    for x in lsgd_inblock:
        xz = ''.join(x)
        lsgd_inblock_year.append(xz+str(data_entry_year))
    
    lsgds = Lsgd.objects.all()
    blocks = Block.objects.filter(block_code = current_block[0]) 
    reqd_data = lsgd_code + str(data_entry_year)
    
    lsgd_mortality = [0,0,0,0]
    block_mortality = [0,0,0,0]

    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
        current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
        current_block_code = current_block[0]
        lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block_code).values_list("lsgd_code")
        lsgd_inblock_year = []
        for x in lsgd_inblock:
            xz = ''.join(x)
            lsgd_inblock_year.append(xz+str(data_entry_year))
        
        blocks = Block.objects.filter(block_code = current_block_code)
        lsgds = Lsgd.objects.all()
        qt = D007.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(live = Sum("S_7_Live_Birth_G") + Sum("S_7_Live_Birth_SC") + Sum("S_7_Live_Birth_ST"))
        lsgd_mortality[0]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(live = Sum("S_7_Neonatal_Death_0_28day_G") + Sum("S_7_Neonatal_Death_0_28day_SC") + Sum("S_7_Neonatal_Death_0_28day_ST"))
        lsgd_mortality[1]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(live = Sum("S_7_Infant_Mortality_0_1_G") + Sum("S_7_Infant_Mortality_0_1_SC") + Sum("S_7_Infant_Mortality_0_1_ST"))
        lsgd_mortality[2]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(live = Sum("S_7_Child_Mortality_1_5_G") + Sum("S_7_Child_Mortality_1_5_SC") + Sum("S_7_Child_Mortality_1_5_ST"))
        lsgd_mortality[3]=qt['live']

        qt = D007.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year  ).aggregate(live = Sum("S_7_Live_Birth_G") + Sum("S_7_Live_Birth_SC") + Sum("S_7_Live_Birth_ST"))
        block_mortality[0]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year  ).aggregate(live = Sum("S_7_Neonatal_Death_0_28day_G") + Sum("S_7_Neonatal_Death_0_28day_SC") + Sum("S_7_Neonatal_Death_0_28day_ST"))
        block_mortality[1]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(live = Sum("S_7_Infant_Mortality_0_1_G") + Sum("S_7_Infant_Mortality_0_1_SC") + Sum("S_7_Infant_Mortality_0_1_ST"))
        block_mortality[2]=qt['live']
        qt = D007.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year  ).aggregate(live = Sum("S_7_Child_Mortality_1_5_G") + Sum("S_7_Child_Mortality_1_5_SC") + Sum("S_7_Child_Mortality_1_5_ST"))
        block_mortality[3]=qt['live']
    
    return render(request, 'analyse/mortality.html', {'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'current_lsgd': current_name, 'blocks': blocks, \
                            'lsgd_selected': lsgd_selected,  'lsgd_data': lsgd_mortality, 'block_data': block_mortality })

def immunization(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]
    lsgd_selected = lsgd_code
    current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
    current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
    lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
    lsgd_inblock_year = []
    for x in lsgd_inblock:
        xz = ''.join(x)
        lsgd_inblock_year.append(xz+str(data_entry_year))
    
    lsgds = Lsgd.objects.all()
    blocks = Block.objects.filter(block_code = current_block[0]) 
    reqd_data = lsgd_code + str(data_entry_year)
    
    immune = [0,0,0]
    vitamin = [0,0,0]
    anemia = [0,0,0]
    worms = [0,0,0]
    rti = [0,0,0]

    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
        current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
        current_block_code = current_block[0]
        lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block_code).values_list("lsgd_code")
        lsgd_inblock_year = []
        for x in lsgd_inblock:
            xz = ''.join(x)
            lsgd_inblock_year.append(xz+str(data_entry_year))
        
        blocks = Block.objects.filter(block_code = current_block_code)
        lsgds = Lsgd.objects.all()
        qt = D005.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcase = Sum("M_Fully_Immunised") + Sum("F_Fully_Immunised"))
        dv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1"))
        immune[0] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        
        qt = D005.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcase = Sum("M_Vitamine_A") + Sum("F_Vitamine_A"))
        dv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcount= Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age"))
        vitamin[0] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)
        
        qt = D005.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcase = Sum("M_Anemia") + Sum("F_Anemia"))
        dv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        anemia[0] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcase = Sum("worms_Infected_M") + Sum("worms_Infected_F"))
        dv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        worms[0] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcase = Sum("M_RTI") + Sum("F_RTI"))
        dv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        rti[0] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)


        qt = D005.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(totcase = Sum("M_Fully_Immunised") + Sum("F_Fully_Immunised"))
        dv = D003.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1"))
        immune[1] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        
        qt = D005.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(totcase = Sum("M_Vitamine_A") + Sum("F_Vitamine_A"))
        dv = D003.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcount= Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age"))
        vitamin[1] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)
        
        qt = D005.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcase = Sum("M_Anemia") + Sum("F_Anemia"))
        dv = D003.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        anemia[1] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcase = Sum("worms_Infected_M") + Sum("worms_Infected_F"))
        dv = D003.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        worms[1] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(totcase = Sum("M_RTI") + Sum("F_RTI"))
        dv = D003.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year).aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        rti[1] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        
        qt = D005.objects.aggregate(totcase = Sum("M_Fully_Immunised") + Sum("F_Fully_Immunised"))
        dv = D003.objects.aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1"))
        immune[2] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        
        qt = D005.objects.aggregate(totcase = Sum("M_Vitamine_A") + Sum("F_Vitamine_A"))
        dv = D003.objects.aggregate(totcount= Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age"))
        vitamin[2] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)
        
        qt = D005.objects.aggregate(totcase = Sum("M_Anemia") + Sum("F_Anemia"))
        dv = D003.objects.aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        anemia[2] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.aggregate(totcase = Sum("worms_Infected_M") + Sum("worms_Infected_F"))
        dv = D003.objects.aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        worms[2] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)

        qt = D005.objects.aggregate(totcase = Sum("M_RTI") + Sum("F_RTI"))
        dv = D003.objects.aggregate(totcount= Sum("children_male_below_age_1") + Sum("children_female_below_age_1") + Sum("children_male_1_to_3_age") + Sum("children_female_1_to_3_age") + Sum("children_male_3_to_5_age") + Sum("children_female_3_to_5_age")  + Sum("children_male_5_to_6_age") + Sum("children_female_5_to_6_age") + Sum("children_male_6_to_10_age") + Sum("children_female_6_to_10_age") + Sum("children_male_10_to_18_age") + Sum("children_female_10_to_18_age"))
        rti[2] = round((( qt['totcase'] / dv['totcount'] ) * 100), 2)
    
    return render(request, 'analyse/immunization.html', {'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'current_lsgd': current_name, 'blocks': blocks, \
                            'lsgd_selected': lsgd_selected, 'immune': immune, 'vitamin': vitamin, 'anemia': anemia, 'worms': worms, 'rti': rti})

def chart(request):
    return render(request, 'analyse/chart.html')

def nutrition(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]
    lsgd_selected = lsgd_code
    current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
    current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
    lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
    lsgd_inblock_year = []
    for x in lsgd_inblock:
        xz = ''.join(x)
        lsgd_inblock_year.append(xz+str(data_entry_year))
    
    lsgds = Lsgd.objects.all()
    blocks = Block.objects.filter(block_code = current_block[0]) 
    reqd_data = lsgd_code + str(data_entry_year)
    
    lsgd_Newborn = [0,0,0,0,0,0]
    lsgdp_Newborn = [0,0,0,0,0,0]
    lsgd_under3 = [0,0,0,0,0,0]
    lsgdp_under3 = [0,0,0,0,0,0]
    lsgd_Three_5 = [0,0,0,0,0,0]
    lsgdp_Three_5 = [0,0,0,0,0,0]

    block_Newborn = [0,0,0,0,0,0]
    blockp_Newborn = [0,0,0,0,0,0]
    block_under3 = [0,0,0,0,0,0]
    blockp_under3 = [0,0,0,0,0,0]
    block_Three_5 = [0,0,0,0,0,0]
    blockp_Three_5 = [0,0,0,0,0,0]



    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
        current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
        current_block_code = current_block[0]
        lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block_code).values_list("lsgd_code")
        lsgd_inblock_year = []
        for x in lsgd_inblock:
            xz = ''.join(x)
            lsgd_inblock_year.append(xz+str(data_entry_year))
        
        blocks = Block.objects.filter(block_code = current_block_code)
        lsgds = Lsgd.objects.all()

        qt = D008.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(Sum("Newborn_measured"), Sum("Newborn_Normal"), Sum("Newborn_Mild"), Sum("Newborn_Moderate"), Sum("Newborn_Severe"))
        yy=0
        for xx in qt:
            lsgd_Newborn[yy] = qt[xx]
            lsgdp_Newborn[yy] = round((lsgd_Newborn[yy]/lsgd_Newborn[0])*100,2)
            yy=yy+1
        lsgd_Newborn[5] = lsgd_Newborn[2] + lsgd_Newborn[3]  + lsgd_Newborn[4] 
        lsgdp_Newborn[5] = round((lsgd_Newborn[5] / lsgd_Newborn[0])*100,2)


        qt = D008.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(Sum("Under3_measured"), Sum("Under3_Normal"), Sum("Under3_Mild"), Sum("Under3_Moderate"), Sum("Under3_Severe"))
        yy=0
        for xx in qt:
            lsgd_under3[yy] = qt[xx]
            lsgdp_under3[yy] = round((lsgd_under3[yy]/lsgd_under3[0])*100,2)
            yy=yy+1
        lsgd_under3[5] = lsgd_under3[2] + lsgd_under3[3]  + lsgd_under3[4] 
        lsgdp_under3[5] = round((lsgd_under3[5] / lsgd_under3[0])*100,2)
      

        qt = D008.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(Sum("Three_5_measured"), Sum("Three_5_Normal"), Sum("Three_5_Mild"), Sum("Three_5_Moderate"), Sum("Three_5_Severe"))
        yy=0
        for xx in qt:
            lsgd_Three_5[yy] = qt[xx]
            lsgdp_Three_5[yy] = round((lsgd_Three_5[yy]/lsgd_Three_5[0])*100,2)
            yy=yy+1
        lsgd_Three_5[5] = lsgd_Three_5[2] + lsgd_Three_5[3]  + lsgd_Three_5[4] 
        lsgdp_Three_5[5] = round((lsgd_Three_5[5] / lsgd_Three_5[0])*100,2)
       
        qt = D008.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(Sum("Newborn_measured"), Sum("Newborn_Normal"), Sum("Newborn_Mild"), Sum("Newborn_Moderate"), Sum("Newborn_Severe"))
        yy=0
        for xx in qt:
            block_Newborn[yy] = qt[xx]
            blockp_Newborn[yy] = round((block_Newborn[yy]/block_Newborn[0])*100,2)
            yy=yy+1
        block_Newborn[5] = block_Newborn[2] + block_Newborn[3]  + block_Newborn[4] 
        blockp_Newborn[5] = round((block_Newborn[5] / block_Newborn[0])*100,2)


        qt = D008.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(Sum("Under3_measured"), Sum("Under3_Normal"), Sum("Under3_Mild"), Sum("Under3_Moderate"), Sum("Under3_Severe"))
        yy=0
        for xx in qt:
            block_under3[yy] = qt[xx]
            blockp_under3[yy] = round((block_under3[yy]/block_under3[0])*100,2)
            yy=yy+1
        block_under3[5] = block_under3[2] + block_under3[3]  + block_under3[4] 
        blockp_under3[5] = round((block_under3[5] / block_under3[0])*100,2)
      

        qt = D008.objects.filter(lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(Sum("Three_5_measured"), Sum("Three_5_Normal"), Sum("Three_5_Mild"), Sum("Three_5_Moderate"), Sum("Three_5_Severe"))
        yy=0
        for xx in qt:
            block_Three_5[yy] = qt[xx]
            blockp_Three_5[yy] = round((block_Three_5[yy]/block_Three_5[0])*100,2)
            yy=yy+1
        block_Three_5[5] = block_Three_5[2] + block_Three_5[3]  + block_Three_5[4] 
        blockp_Three_5[5] = round((block_Three_5[5] / block_Three_5[0])*100,2)

    lsgd_data=[lsgd_Newborn,lsgdp_Newborn,lsgd_under3,lsgdp_under3,lsgd_Three_5,lsgdp_Three_5]
    block_data=[block_Newborn,blockp_Newborn,block_under3,blockp_under3,block_Three_5,blockp_Three_5]

    return render(request, 'analyse/nutrition.html', {'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'current_lsgd': current_name, 'blocks': blocks, \
                            'lsgd_selected': lsgd_selected,  'lsgd_data': lsgd_data, 'block_data': block_data })

def ecce(request):
    data_entry_year = 2018
    current_user = request.user
    lsgd_code = current_user.profile.user_lsgd
    district_code = lsgd_code[:5]
    lsgd_selected = lsgd_code
    current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
    current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
    lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block[0]).values_list("lsgd_code")
    lsgd_inblock_year = []
    for x in lsgd_inblock:
        xz = ''.join(x)
        lsgd_inblock_year.append(xz+str(data_entry_year))
    
    lsgds = Lsgd.objects.all()
    blocks = Block.objects.filter(block_code = current_block[0]) 
    reqd_data = lsgd_code + str(data_entry_year)
    
    lsgd_count = [0,0,0,0,0,0,0,0]
    lsgd_per = [0,0,0,0,0,0,0,0]
    block_count = [0,0,0,0,0,0,0,0]
    block_per = [0,0,0,0,0,0,0,0]
    dist_count = [0,0,0,0,0,0,0,0]
    dist_per = [0,0,0,0,0,0,0,0]

    if request.method == 'POST':
        lsgd_selected = request.POST.get('lsgd_selected')
        reqd_data = lsgd_selected + str(data_entry_year)
        current_block = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_block', flat=True)
        current_name = Lsgd.objects.filter(lsgd_code = lsgd_selected).values_list('lsgd_name', flat=True)
        current_block_code = current_block[0]
        lsgd_inblock = Lsgd.objects.filter(lsgd_block = current_block_code).values_list("lsgd_code")
        lsgd_inblock_year = []
        for x in lsgd_inblock:
            xz = ''.join(x)
            lsgd_inblock_year.append(xz+str(data_entry_year))
        
        blocks = Block.objects.filter(block_code = current_block_code)
        lsgds = Lsgd.objects.all()
        qt = D009.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(Sum("Entolled_Pre_school_AW"),Sum("Enrolled_other_PreSchool"),Sum("AW_Nutrition_3_5"),Sum("Enrolled_AW_SNP"))
        qv = D003.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(one2three=Sum("children_male_1_to_3_age")+Sum("children_female_1_to_3_age"),three2five=Sum('children_male_3_to_5_age')+Sum('children_female_3_to_5_age'))
        lsgd_count[0]=qv['one2three']
        lsgd_count[1]=qv['three2five']
        lsgd_count[2]=qt['Entolled_Pre_school_AW__sum']
        lsgd_per[2]=round((qt['Entolled_Pre_school_AW__sum']/qv['three2five'])*100,2)
        lsgd_count[3]=qt['Enrolled_other_PreSchool__sum']
        lsgd_per[3]=round((qt['Enrolled_other_PreSchool__sum']/qv['three2five'])*100,2)
        lsgd_count[4] = lsgd_count[1] - (lsgd_count[2]+lsgd_count[3])
        lsgd_per[4]=round((lsgd_count[4]/qv['three2five'])*100,2)
        lsgd_count[5]=qt['AW_Nutrition_3_5__sum']
        lsgd_per[5]=round((qt['AW_Nutrition_3_5__sum']/qv['three2five'])*100,2)
        lsgd_count[6]=qt['Enrolled_AW_SNP__sum']
        lsgd_per[6]=round((qt['Enrolled_AW_SNP__sum']/qv['one2three'])*100,2)  
        qv = D006.objects.filter(lsgd_code_and_year = reqd_data ).aggregate(ebf=Sum("EBF_Mothers_G")+Sum("EBF_Mothers_SC")+Sum("EBF_Mothers_ST"))
        lsgd_count[7]=qv['ebf']
        lsgd_per[7]=round((lsgd_count[7]/lsgd_count[0])*100,2)  

        qt = D009.objects.filter( lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(Sum("Entolled_Pre_school_AW"),Sum("Enrolled_other_PreSchool"),Sum("AW_Nutrition_3_5"),Sum("Enrolled_AW_SNP"))
        qv = D003.objects.filter( lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(one2three=Sum("children_male_1_to_3_age")+Sum("children_female_1_to_3_age"),three2five=Sum('children_male_3_to_5_age')+Sum('children_female_3_to_5_age'))
        block_count[0]=qv['one2three']
        block_count[1]=qv['three2five']
        block_count[2]=qt['Entolled_Pre_school_AW__sum']
        block_per[2]=round((qt['Entolled_Pre_school_AW__sum']/qv['three2five'])*100,2)
        block_count[3]=qt['Enrolled_other_PreSchool__sum']
        block_per[3]=round((qt['Enrolled_other_PreSchool__sum']/qv['three2five'])*100,2)
        block_count[4] = block_count[1] - (block_count[2]+block_count[3])
        block_per[4]=round((block_count[4]/qv['three2five'])*100,2)
        block_count[5]=qt['AW_Nutrition_3_5__sum']
        block_per[5]=round((qt['AW_Nutrition_3_5__sum']/qv['three2five'])*100,2)
        block_count[6]=qt['Enrolled_AW_SNP__sum']
        block_per[6]=round((qt['Enrolled_AW_SNP__sum']/qv['one2three'])*100,2)  
        qv = D006.objects.filter( lsgd_code_and_year__in=lsgd_inblock_year ).aggregate(ebf=Sum("EBF_Mothers_G")+Sum("EBF_Mothers_SC")+Sum("EBF_Mothers_ST"))
        block_count[7]=qv['ebf']
        block_per[7]=round((block_count[7]/block_count[0])*100,2)  

        qt = D009.objects.aggregate(Sum("Entolled_Pre_school_AW"),Sum("Enrolled_other_PreSchool"),Sum("AW_Nutrition_3_5"),Sum("Enrolled_AW_SNP"))
        qv = D003.objects.aggregate(one2three=Sum("children_male_1_to_3_age")+Sum("children_female_1_to_3_age"),three2five=Sum('children_male_3_to_5_age')+Sum('children_female_3_to_5_age'))
        dist_count[0]=qv['one2three']
        dist_count[1]=qv['three2five']
        dist_count[2]=qt['Entolled_Pre_school_AW__sum']
        dist_per[2]=round((qt['Entolled_Pre_school_AW__sum']/qv['three2five'])*100,2)
        dist_count[3]=qt['Enrolled_other_PreSchool__sum']
        dist_per[3]=round((qt['Enrolled_other_PreSchool__sum']/qv['three2five'])*100,2)
        dist_count[4] = dist_count[1] - (dist_count[2]+dist_count[3])
        dist_per[4]=round((dist_count[4]/qv['three2five'])*100,2)
        dist_count[5]=qt['AW_Nutrition_3_5__sum']
        dist_per[5]=round((qt['AW_Nutrition_3_5__sum']/qv['three2five'])*100,2)
        dist_count[6]=qt['Enrolled_AW_SNP__sum']
        dist_per[6]=round((qt['Enrolled_AW_SNP__sum']/qv['one2three'])*100,2)  
        qv = D006.objects.aggregate(ebf=Sum("EBF_Mothers_G")+Sum("EBF_Mothers_SC")+Sum("EBF_Mothers_ST"))
        dist_count[7]=qv['ebf']
        dist_per[7]=round((dist_count[7]/dist_count[0])*100,2) 
        
    lsgd_data = [lsgd_count,lsgd_per]
    block_data = [block_count,block_per]
    dist_data = [dist_count,dist_per]
    return render(request, 'analyse/ecce.html', {'lsgds': lsgds, 'data_entry_year': data_entry_year, \
                            'current_user': current_user, 'current_lsgd': current_name, 'blocks': blocks, \
                            'lsgd_selected': lsgd_selected,  'lsgd_data': lsgd_data, 'block_data': block_data, 'dist_data': dist_data })
