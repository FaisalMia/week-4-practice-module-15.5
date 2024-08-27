from django.db import models
from musician_app.models import Musician
# from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Musician,on_delete=models.CASCADE)
    release_date = models.DateField()
    CHOICES = [(1,1),(2,2),(3,3),(4,4),(5,5)]
    rating = models.PositiveSmallIntegerField(choices=CHOICES,default=0)
    # (validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    def __str__(self):
        return self.name
    
    