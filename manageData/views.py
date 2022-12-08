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
        item_list = execute_query("SELECT * FROM DESTINATION_AREA")
    elif (idcommand=="site"):
        saved_values = ["Site", "Destination Area", "Nama", "add-"+idcommand]
        item_list = execute_query("""SELECT DISTINCT SITE.id, SITE.destareaid, SITE.name, 
        SITE.description, SITE.image, DESTINATION_AREA.province, DESTINATION_AREA.name
        FROM SITE, DESTINATION_AREA WHERE SITE.destareaid = DESTINATION_AREA.id""")
        print(item_list)
    elif (idcommand=="accommodation"):
        saved_values = ["Accommodation", "Destination Area", "Nama", "add-"+idcommand]
        item_list = execute_query("""SELECT DISTINCT ACCOMMODATION.id, ACCOMMODATION.destareaid, ACCOMMODATION.name, 
        ACCOMMODATION.description, ACCOMMODATION.image, DESTINATION_AREA.province, DESTINATION_AREA.name, ACCOMMODATION.price
        FROM ACCOMMODATION, DESTINATION_AREA WHERE ACCOMMODATION.destareaid = DESTINATION_AREA.id""")
        print(item_list)
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

    item_list = execute_query("""SELECT DISTINCT DESTINATION_AREA.id, DESTINATION_AREA.province, DESTINATION_AREA.name 
    FROM SITE, DESTINATION_AREA WHERE DESTINATION_AREA.id IN (SELECT destareaid FROM SITE)""")

    if request.method == 'POST':
        form = SiteForm(item_list, request.POST)
        if form.is_valid():
            dest_area = form.cleaned_data['dest_area']
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
        form = SiteForm(item_list)

    return render(request, 'add_site.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def add_accommodation(request):

    item_list = execute_query("""SELECT DISTINCT DESTINATION_AREA.id, DESTINATION_AREA.province, DESTINATION_AREA.name 
    FROM ACCOMMODATION, DESTINATION_AREA WHERE DESTINATION_AREA.id IN (SELECT destareaid FROM ACCOMMODATION)""")

    if request.method == 'POST':
        form = AccommodationForm(item_list, request.POST)
        if form.is_valid():
            dest_area = form.cleaned_data['dest_area']
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
        form = AccommodationForm(item_list)

    return render(request, 'add_accommodation.html', {'form': form})