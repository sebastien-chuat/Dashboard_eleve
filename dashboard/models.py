from django.db import models
from django.contrib.auth.models import User

class Student(User):    
    def __str__(self):
        return '%s %s' % (self.prenom, self.nom)

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie')
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre


class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    difficulty = models.IntegerField()
    

    ## J'ai commenté les trois lignes suivantes: (Sébastien) ##

    # author = models.ForeignKey('Teacher', related_name="courses")
    # chapter = models.ForeignKey('Chapter', related_name="courses")
    # favorites = models.ManyToManyField(User, related_name="favorite_courses", blank=True, null=True)
    
    ## Celles-là l'étaient déjà ##

    # videos = models.ManyToManyField(Video)
    # images = models.ManyToManyField(Image)
    # definitions = models.ManyToManyField(Definition)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name

    def total_pages(self):
        return self.pages.count()