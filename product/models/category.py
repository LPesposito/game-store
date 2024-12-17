from django.db import models 


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripstion = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.title