from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http.response import HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def home_admin(request):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM ADMIN;")
        result = namedtuplefetchall(cursor)
        print(result)
    return render(request, 'home_admin.html')
