from django.shortcuts import render


# Create your views here.
def web_page(request):
    return render(request, 'web/index.html')
    