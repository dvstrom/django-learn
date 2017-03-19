from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def getviews(self):
        return self.views

    def getlikes(self):
        return self.likes
    
    def setview(self, views):
        self.views = views

    def setlikes(self, likes):
        self.likes = likes

    def __unicode__(self):
        return self.name

    
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode(self):
        return self.title
    
        
    
    
    
    




