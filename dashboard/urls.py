from django.conf.urls import patterns, include, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', 'home'),  # Accueil du dashboard
    url(r'^course/(?P<id_course>\d+)$', 'view_course'),  # Vue d'un cours
    url(r'^cours', 'list_cours'),  # Vue des cours d'une branche précise
    url(r'^date$', 'date_actuelle')
)