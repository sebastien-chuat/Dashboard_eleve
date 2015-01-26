from django.conf.urls import patterns, include, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', 'home'),  # Accueil du dashboard
    url(r'^course/(?P<id_course>\d+)$', 'view_course'),  # Vue d'un cours
    url(r'^courses/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles'),  # Vue des courss d'une branche précise
    url(r'^date$', 'date_actuelle')
)