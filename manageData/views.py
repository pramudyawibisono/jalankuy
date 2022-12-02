from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from .forms import *

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

def home_admin(request):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM ADMIN;")
        result = namedtuplefetchall(cursor)
        print(result)
    return render(request, 'home_admin.html')

def view_destination_area(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM DESTINATION_AREA"
    destination_area_list = execute_query(query)
    # print(accommodation_list) # debug

    context = {'destination_area_list': destination_area_list}
    print(context) # debug

    return render(request, 'destination_area_list.html', context)

def view_site(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM SITE"
    site_list = execute_query(query)
    # print(accommodation_list) # debug

    context = {'site_list': site_list}
    print(context) # debug

    return render(request, 'site_list.html', context)


def view_accommodation(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION"
    accommodation_list = execute_query(query)
    # print(accommodation_list) # debug

    context = {'accommodation_list': accommodation_list}
    print(context) # debug

    return render(request, 'accommodation_list.html', context)

def add_destination_area(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
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
            return HttpResponseRedirect(f'view-destination-area')
    else:
        form = DestinationAreaForm()

    return render(request, 'add_destination_area.html', {'form': form})

def add_site(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
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
            return HttpResponseRedirect(f'view-site')
    else:
        form = SiteForm()

    return render(request, 'add_site.html', {'form': form})

def add_accommodation(request):
    #TODO Cek udah login atau belum. Kalo belum, redirect ke login page
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
            return HttpResponseRedirect(f'view-accommodation')
    else:
        form = AccommodationForm()

    return render(request, 'add_accommodation.html', {'form': form})

