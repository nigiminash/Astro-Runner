from django.db import models

# Create your models here.
class User(models.Model):
    vorname = models.CharField(max_length = 100)
    nachname = models.CharField(max_length = 100)
    email = models.CharField(null = True, max_length = 100)
    termin = models.DateField(null = True)

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

class News(models.Model):
    heading = models.CharField(max_length = 100)
    text = models.CharField(max_length = 500)
    pic = models.ImageField(null = True, blank = True, max_length=100, upload_to = 'media')

    def __str__(self):
        return f"{self.heading}"

class Jobs(models.Model):
    prof = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    requirements = models.CharField(max_length = 300)
    pic = models.ImageField(null = True, blank = True, max_length=100, upload_to = 'media')

    def __str__(self):
        return f"{self.prof}"
                
