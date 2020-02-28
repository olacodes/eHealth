from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from ..forms.user_medical_form import UserMedicalForm, UserMedicalFormUpdate

def is_staff_check(user):
    return not user.is_staff

@user_passes_test(is_staff_check, redirect_field_name='dashboard')
@login_required
def user_medical_info(request):
    
    if request.method == 'POST':
        u_form = UserMedicalForm(request.POST, instance=request.user)
        p_form = UserMedicalFormUpdate(request.POST, instance=request.user.medicalinformation) 
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You medical information has been successfully updated!')
            return redirect('dashboard')

    else:
        u_form = UserMedicalForm(instance=request.user)
        p_form = UserMedicalFormUpdate(instance=request.user.medicalinformation) 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/med_info.html', context)
    