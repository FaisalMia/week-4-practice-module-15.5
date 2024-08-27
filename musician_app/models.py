from django.db import models

# Create your models here.
class Musician(models.Model):
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_nmb = models.CharField(max_length=11)
    instrument_type = models.TextField()
    
    
    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"
    
    
    
