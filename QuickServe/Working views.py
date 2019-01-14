from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.contrib.auth.forms import User
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
# from Accounts.forms import SignUpForm, EditProfileForm, ProfileData
from django.utils.timezone import now

from QuickServe.forms import ClockinForm, AgencyForm, DepartmentForm, ExtraForm, SignUpForm
from QuickServe.models import Attendance, Agency, Department, Profile


@login_required
def home(request):
    return render(request, 'homep/home.html')


@login_required
def clockin(request):
    if request.method == 'POST':
        form = ClockinForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')


@login_required
def agency_list(request):
    # agencys = Agency.objects.all().order_by("id") # to order in ascending order
    agencys = Agency.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'agencys/agency_list.html', {'agencys': agencys})


# AGENCY VIEWS

@login_required
def save_agency_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            agencys = Agency.objects.all().order_by("-id")
            paginator = Paginator(agencys, 12)
            data['html_agency_list'] = render_to_string('agencys/includes/partial_agency_list.html', {
                'agencys': agencys
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def agency_create(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST)
    else:
        form = AgencyForm()
    return save_agency_form(request, form, 'agencys/includes/partial_agency_create.html')


@login_required
def agency_update(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=agency)
    else:
        form = AgencyForm(instance=agency)
    return save_agency_form(request, form, 'agencys/includes/partial_subject_update.html')


@login_required
def agency_delete(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    data = dict()
    if request.method == 'POST':
        agency.delete()
        data['form_is_valid'] = True
        agencys = Agency.objects.all().order_by("-id")
        paginator = Paginator(agencys, 12)
        data['html_agency_list'] = render_to_string('agencys/includes/partial_agency_list.html', {
            'agencys': agencys
        })
    else:
        context = {'agency': agency}
        data['html_form'] = render_to_string('agencys/includes/partial_agency_delete.html', context, request=request)
    return JsonResponse(data)


# Department Views


@login_required
def department_list(request):
    # departments = Department.objects.all().order_by("id") # to order in ascending order
    departments = Department.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'departments/department_list.html', {'departments': departments})


# AGENCY VIEWS

@login_required
def save_department_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            departments = Department.objects.all().order_by("-id")
            paginator = Paginator(departments, 12)
            data['html_department_list'] = render_to_string('departments/includes/partial_department_list.html', {
                'departments': departments
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
    else:
        form = DepartmentForm()
    return save_department_form(request, form, 'departments/includes/partial_department_create.html')


@login_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
    else:
        form = DepartmentForm(instance=department)
    return save_department_form(request, form, 'departments/includes/partial_department_update.html')


@login_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    data = dict()
    if request.method == 'POST':
        department.delete()
        data['form_is_valid'] = True
        departments = Department.objects.all().order_by("-id")
        paginator = Paginator(departments, 12)
        data['html_department_list'] = render_to_string('departments/includes/partial_department_list.html', {
            'departments': departments
        })
    else:
        context = {'department': department}
        data['html_form'] = render_to_string('departments/includes/partial_department_delete.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def profile_list(request):
    # profiles = Profile.objects.all().order_by("id") # to order in ascending order
    users = User.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'profiles/profile_list.html', {'users': users})


# AGENCY VIEWS

@transaction.atomic
def createUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        extra = ExtraForm(request.POST, request.FILES)
        if form.is_valid() and extra.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            extra = ExtraForm(request.POST, request.FILES,
                                instance=user.profile)  # Reload the profile form with the profile instance
            extra.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            extra.save()  # Gracefully save the form
        else:
            return redirect('home')
    else:
        form = SignUpForm()
        extra = ExtraForm()
    return render(request, 'profiles/createUser.html', {'form': form, 'extra': extra})


"""  

@login_required
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
    else:
        form = ProfileForm(instance=profile)
    return save_profile_form(request, form, 'profiles/includes/partial_profile_update.html')


@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    data = dict()
    if request.method == 'POST':
        profile.delete()
        data['form_is_valid'] = True
        users = User.objects.all().order_by("-id")
        paginator = Paginator(users, 12)
        data['html_profile_list'] = render_to_string('profiles/includes/partial_profile_list.html', {
            'users': users
        })
    else:
        context = {'profile': profile}
        data['html_form'] = render_to_string('profiles/includes/partial_profile_delete.html', context, request=request)
    return JsonResponse(data)

"""
