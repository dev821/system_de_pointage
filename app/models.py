from django.db import models

from datetime import datetime
# Create your models here.

class Employe(models.Model):
  firstName = models.CharField('Nom',max_length=255)
  lastName = models.CharField('Prenom', max_length=255)
  address =  models.CharField('Residence', max_length = 255)
  tel = models.CharField('Numero De Telephone', max_length=10, unique=True)
  hashed = models.CharField('HASH', max_length = 255)
  
  class Meta:
    ordering = ['lastName', 'firstName']
  
  def __str__(self):
    """String for representing the Model object."""
    return self.firstName + ' ' + self.lastName


class Pointage(models.Model):
  idEmploye = models.ForeignKey('Employe',  on_delete=models.RESTRICT, null = False)
  dateEmprunt = models.DateTimeField( verbose_name ='Date De Emprunt',default=datetime.now ) # when we register the presance of a person the database will fullfill this attribute automatically and assign it to the moment of inserting the tuple
  presence = (
    ('p', 'Present(e)'),
    ('a', 'Absent(e)')
  )
  
  status = models.CharField('Status',
    max_length = 1,
    choices = presence,
    default='n',
    help_text='la disponibilté de l\'employé(e)'
  )
  
  class Meta :
    ordering = ['dateEmprunt']
  
  def __str__(self):
    """String for representing the Model object."""
    return f'{self.idEmploye}'
