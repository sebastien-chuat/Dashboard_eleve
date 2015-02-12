from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def view_course(request, id_course):
    """ je dois trouver comment afficher un cours ici"""

    return render(request, '')

def list_cours(request):
    """ Liste des cours. """

    return render (request, 'dashboard/cours.html')



## ICI c'est vraiment à quoi ça doit ressembler ! Et non pas avec des HttpResponse ##

def date_actuelle(request):
    return render (request, 'dashboard/date.html')