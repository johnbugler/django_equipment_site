from django.shortcuts import render, redirect
from .models import Device
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewDeviceForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
    """
    View function for home page of site.
    """

    devices_list = Device.objects.all()

    query = request.GET.get("q")
    if query:
        devices_list = devices_list.filter(
            Q(equipment__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(email__icontains=query)
        )

#    paginator = Paginator(devices_list, 3)
#
#    page = request.GET.get('page')
#    try:
#        devices = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver first page.
#        devices = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range (e.g. 9999), deliver last page of results.
#        devices = paginator.page(paginator.num_pages)

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'devices_list':devices_list},
    )

def ads(request):
    """
    View function for advertisements page of site.
    """

    return render(
        request,
        'ads.html',
    )

def contact(request):
    """
    View function for contact details.
    """

    return render(
        request,
        'contact.html',
    )

def signup(request):
    """
    View function for signing up.
    """

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(
        request,
        'signup.html',
        {'form': form},
    )

@login_required
def DevicesByUserView(request):
    """
    View function for listing devices of current user. 
    """
    userdevices=Device.objects.filter(researcher=request.user)
    template_name ='devices_user.html'

    return render(
        request,
        'devices_user.html',
        context={'userdevices':userdevices},
    )

@login_required
def NewDevice(request):
    """
    View function for adding devices.
    """

    if request.method == 'POST':
        form = NewDeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            device.researcher = request.user
            device.save()
            return redirect('my-devices')
    else:
        form = NewDeviceForm()

    return render(
        request,
        'newdevice.html',
        {'form': form},
    )

def delete(request, id):
    device = Device.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('my-devices'))