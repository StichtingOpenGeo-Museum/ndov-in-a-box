from django.db import models
from django.contrib.auth.models import User

class Koppelvlak6(models.Model):
    dataowner = models.ForeignKey(User)
    sourceip = models.IPAddressField('Bron IPv4 adres')
    destinationport = models.IntegerField('Doel Poort')
    
