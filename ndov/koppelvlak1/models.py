from django.db import models
from django.contrib.auth.models import User

class Koppelvlak1(models.Model):
    dataowner = models.ForeignKey(User)
    filename = models.FileField('Bestandsnaam', max_length=32, upload_to='/var/www/kv1')
    pub_date = models.DateTimeField('Upload Datum')
    valid_from_date = models.DateField('Ingangsdatum')
    
    CHARACTER_ENCODINGS = (
        ('UTF-8', 'UTF-8'),
        ('UNICODE', 'Unicode'),
        ('CP1252', 'Codepage 1252'),
    )
    character_encoding = models.CharField('Tekst Encodering', max_length=5, choices=CHARACTER_ENCODINGS)

class Concession(models.Model):
    koppelvlak1 = models.ForeignKey(Koppelvlak1)
    concession_name = models.CharField('Concessie', max_length=16)
