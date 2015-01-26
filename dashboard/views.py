from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """
    <h1>Bienvenue sur Webmath !</h1>
    <p>Ici sera présent le Dashboard</p>"""
    return HttpResponse(text)

def view_course(request, id_course):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
        Son ID est le second paramètre de la fonction (pour rappel, le premier
        paramètre est TOUJOURS la requête de l'utilisateur) """

    text = "Vous avez demandé le cours #{0} !".format(id_course)
    if int(id_course) > 100:
    	raise Http404
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def date_actuelle(request):
    return render (request, 'dashboard/date.html', {'date': datetime.now()})