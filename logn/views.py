from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User
from logn.models import Profile
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home', {'current_user': request.user})
        else:
            return redirect('/login')
    else:
        return render(request, 'r2n2/login.html')

def year_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home', {'current_user': request.user})
        else:
            return redirect('/login')
    else:
        return render(request, 'r2n2/login.html')

def home_page(request):
    return render(request, 'r2n2/index.html', {'current_user': request.user})
	
def logout_page(request):
	logout(request)
	return render(request, 'r2n2/login.html')

def lang_page(request):
    language_selected = 0

    if request.method == 'POST':
        language_selected = request.POST.get('language_selected')
    else:
        language_selected = 0
        
    current_user = request.user
    current_user.profile.user_lang = language_selected
    current_user.profile.save()

    print(current_user.profile.user_lang)

    return render(request, 'logn/lang.html', {'language_selected': language_selected})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('/home')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'r2n2/passwordchange.html', {'form': form})

def contacts_page(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    users_and_profiles = zip(users, profiles)
    print(profiles)
    return render(request, 'logn/cont.html', {'users_and_profiles': users_and_profiles})

