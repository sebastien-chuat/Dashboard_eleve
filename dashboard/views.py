from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def view_course(request, id_course):
    """ je dois trouver comment afficher un cours ici"""

    return render(request, '')

def list_cours(request):
    """ Liste des cours. """

    return render (request, 'cours.html')

def date_actuelle(request):
    return render (request, 'date.html')