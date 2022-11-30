from django.shortcuts import render
from .forms import *
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.db import connection
from collections import namedtuple

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

def accommodations(request, destareaid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid};"
    accommodation_list = execute_query(query)
    # print(accommodation_list) # debug

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {destareaid}"
    dest_area_name = execute_query(query)[0][0]
    # print(dest_area_name) # debug

    context = {'accommodation_list': accommodation_list, 'dest_area_name': dest_area_name}
    print(context) # debug

    return render(request, 'accommodation_list.html', context)

def accommodation_detail(request, destareaid, accommid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid} AND id = {accommid};"
    accommodation = execute_query(query)[0]
    # print(accommodation) # debug

    query = f"SELECT * FROM ACCOMMODATION_REVIEW WHERE accommodationID = {accommid};"
    reviews = execute_query(query)
    # print(reviews) # debug

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {destareaid}"
    dest_area_name = execute_query(query)[0][0]
    # print(dest_area_name) # debug

    context = {
        'accommodation': accommodation, 
        'reviews': reviews, 
        'dest_area_name': dest_area_name,
        'ids': [destareaid, accommid]
        }
    print(context) # debug

    return render(request, 'accommodation_detail.html', context)

def add_accommodation_review(request, destareaid, accommid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    reviewer = 'pram2' # debug, dummy value 
    if request.method == 'POST':
        form = AccommodationReviewForm(request.POST)
        if form.is_valid():
            score = int(form.cleaned_data['score'])
            comment = form.cleaned_data['comment']
            query = f"INSERT INTO ACCOMMODATION_REVIEW VALUES (\
                DEFAULT, {accommid}, '{reviewer}', {score}, '{comment}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan review") # debug
            return HttpResponseRedirect(f'/destination-area/{destareaid}/accommodations/{accommid}')
    else:
        form = AccommodationReviewForm()

    return render(request, 'add_accommodation_review.html', {'form': form})