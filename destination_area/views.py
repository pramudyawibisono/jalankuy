from django.shortcuts import render

# Create your views here.

from django.db import connection
from collections import namedtuple
from .forms import *;

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

def destinations(request):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM DESTINATION_AREA"
    destination_area_list = execute_query(query)
    # print(accommodation_list) # debug

    context = {'destination_area_list': destination_area_list}
    print(context) # debug

    return render(request, 'destination_area_list.html', context)

def destination_detail(request, id):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM DESTINATION_AREA WHERE ID = {id}"
    destination = execute_query(query)[0]
    # print(accommodation) # debug

    query = f"SELECT * FROM DEST_AREA_REVIEW WHERE ID = {id};"
    reviews = execute_query(query)
    # print(reviews) # debug

    context = {
        'dest_area': destination, 
        'reviews': reviews, 
        'id': id
        }
    print(context) # debug

    return render(request, 'destination_area_detail.html', context)

def add_destination_area_review(request, id):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    reviewer = 'anonymous' # debug, dummy value 
    if request.method == 'POST':
        form = DestinationAreaReviewForm(request.POST)
        if form.is_valid():
            score = int(form.cleaned_data['score'])
            comment = form.cleaned_data['comment']
            query = f"INSERT INTO DEST_AREA_REVIEW VALUES (\
                DEFAULT, {id}, '{reviewer}', {score}, '{comment}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan review") # debug
            return HttpResponseRedirect(f'/destination-area/{id}')
    else:
        form = DestinationAreaReviewForm()

    return render(request, 'add_destination_area_review.html', {'form': form})