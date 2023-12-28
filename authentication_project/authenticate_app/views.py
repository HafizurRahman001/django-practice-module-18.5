from django.shortcuts import render,redirect
from authenticate_app.forms import UpdateUserData
from authenticate_app.forms import SignUPForm, UpdateUserData
from django.contrib.auth import login, logout, update_session_auth_hash,authenticate
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        signup_form = SignUPForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
    else:
        signup_form = SignUPForm()
    return render(request,'data_change_form.html', {'form':signup_form, 'type':'Signup'})


def profile(request):
    return render(request,'profile.html')



def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request = request, data = request.POST)
        if login_form.is_valid():
            userName = login_form.cleaned_data['username']
            userPass = login_form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user is not None:
                messages.success(request, "Loged in Successfully")
                login(request,user)
                return redirect('profile')
    else:
        login_form = AuthenticationForm()
    return render(request,'data_change_form.html', {'form':login_form, 'type':'Login'})



def user_logout(request):
    logout(request)
    messages.success(request, "Loged out successfully")
    return redirect('user_login')



def change_password_by_old_password(request):
    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(user= request.user, data = request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, "Password change Successfully")
            update_session_auth_hash(request, change_pass_form.user)
            return redirect('profile')
    else:
        change_pass_form = PasswordChangeForm(user = request.user)
    return render(request,'data_change_form.html',{'form':change_pass_form,'type':'Password change'})



def change_password_without_old_password(request):
    if request.method == 'POST':
        change_pass_form = SetPasswordForm(user= request.user, data = request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, "Password change Successfully")
            update_session_auth_hash(request, change_pass_form.user)
            return redirect('profile')
    else:
        change_pass_form = SetPasswordForm(user = request.user)
    return render(request,'data_change_form.html',{'form':change_pass_form,'type':'Password change'})




def update_user_data(request):
    if request.method == 'POST':
        update_data_form = UpdateUserData(request.POST, instance=request.user)
        if update_data_form.is_valid():
            update_data_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('profile')
    else:
        update_data_form = UpdateUserData(instance=request.user)
    return render(request,'data_change_form.html',{'form':update_data_form,'type':'Profile Update'})