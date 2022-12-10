from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.db import connection
from .forms import *
from .helper import *

# Create your views here.

@login_required(login_url='/auth/login')
def accommodations(request, destareaid):
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid};"
    accommodation_list = execute_query(query)

    if accommodation_list == []:
        return HttpResponseNotFound("Data is not exist, please go back to previous page")

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {destareaid}"
    dest_area_name = execute_query(query)[0][0]

    context = {'accommodation_list': accommodation_list, 'dest_area_name': dest_area_name}

    return render(request, 'accommodation_list.html', context)


@login_required(login_url='/auth/login')
def accommodation_detail(request, destareaid, accommid):
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid} AND id = {accommid};"
    accommodation = execute_query(query)

    if accommodation == []:
        return HttpResponseNotFound("Data is not exist, please go back to previous page")
    
    accommodation = accommodation[0]

    query = f"SELECT * FROM ACCOMMODATION_REVIEW WHERE accommodationID = {accommid};"
    reviews = execute_query(query)

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {destareaid}"
    dest_area_name = execute_query(query)[0][0]

    context = {
        'accommodation': accommodation, 
        'reviews': reviews, 
        'dest_area_name': dest_area_name,
        'ids': [destareaid, accommid]
        }

    return render(request, 'accommodation_detail.html', context)


@login_required(login_url='/auth/login')
def add_accommodation_review(request, destareaid, accommid):
    reviewer = request.user
    if request.method == 'POST':
        form = AccommodationReviewForm(request.POST)
        if form.is_valid():
            score = int(form.cleaned_data['score'])
            comment = form.cleaned_data['comment']
            query = f"INSERT INTO ACCOMMODATION_REVIEW VALUES (\
                DEFAULT, {accommid}, '{reviewer}', {score}, '{comment}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return HttpResponseRedirect(f'/{destareaid}/accommodations/{accommid}')
    else:
        form = AccommodationReviewForm()

    return render(request, 'add_accommodation_review.html', {'form': form})