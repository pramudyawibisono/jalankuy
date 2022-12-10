from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from .forms import *

from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def execute_query(query):
    result = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def home_admin(request):

    return render(request, 'home_admin.html')

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def view_all_list(request, idcommand):

    if (idcommand=="destination-area"):
        saved_values = ["Destination Area", "Provinsi", "Kota", "add-"+idcommand]
        item_list = execute_query(f"SELECT * FROM DESTINATION_AREA")
    elif (idcommand=="site"):
        saved_values = ["Site", "Destination Area ID", "Nama", "add-"+idcommand]
        item_list = execute_query(f"SELECT * FROM SITE")
    elif (idcommand=="accommodation"):
        saved_values = ["Accommodation", "Destination Area ID", "Nama", "add-"+idcommand]
        item_list = execute_query(f"SELECT * FROM ACCOMMODATION")
    else:
        return home_admin(request)
    
    context = {'item_list':item_list, 'saved_values':saved_values}

    return render(request, 'admin_all_list.html', context)

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def add_destination_area(request):

    if request.method == 'POST':
        form = DestinationAreaForm(request.POST)
        if form.is_valid():
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']
            desc = form.cleaned_data['desc']
            pic = form.cleaned_data['pic']
            query = f"INSERT INTO DESTINATION_AREA VALUES (\
                DEFAULT, '{province}', '{city}', '{desc}', '{pic}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan destination area") # debug

            return HttpResponseRedirect(f'view/destination-area')
    else:
        form = DestinationAreaForm()

    return render(request, 'add_destination_area.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def add_site(request):

    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            dest_area = int(form.cleaned_data['dest_area'])
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            pic = form.cleaned_data['pic']
            query = f"INSERT INTO SITE VALUES (\
                DEFAULT, {dest_area}, '{name}', '{desc}', '{pic}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan site") # debug

            return HttpResponseRedirect(f'view/site')
    else:
        form = SiteForm()

    return render(request, 'add_site.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def add_accommodation(request):

    if request.method == 'POST':
        form = AccommodationForm(request.POST)
        if form.is_valid():
            dest_area = int(form.cleaned_data['dest_area'])
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            pic = form.cleaned_data['pic']
            price = int(form.cleaned_data['price'])
            query = f"INSERT INTO ACCOMMODATION VALUES (\
                DEFAULT, {dest_area}, '{name}', '{desc}', '{pic}', {price});"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan accommodation") # debug

            return HttpResponseRedirect(f'view/accommodation')
    else:
        form = AccommodationForm()

    return render(request, 'add_accommodation.html', {'form': form})