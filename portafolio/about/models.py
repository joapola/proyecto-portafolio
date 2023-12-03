from django.db import models

# Create your models here.
#Modelo para Formacion academica = Course
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Titulo')
    degree_title = models.CharField(max_length=400, verbose_name= 'Titulo obtenido')
    description = models.TextField(verbose_name= 'Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de Modificacion')
    
    #Convertir en español la aplicacion en el admin y ordenar en los registros
    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ['-created']
    # Para que muestre el titulo del proyecto que agregamos     
    def __str__(self):
        return self.title 


#Modelo para los conocimientos = Skill
class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Titulo')
    image = models.ImageField(upload_to='skills', verbose_name= 'Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de Modificacion')

  #Convertir en español la aplicacion en el admin y ordenar en los registros
    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created']
    # Para que muestre el titulo del proyecto que agregamos     
    def __str__(self):
        return self.title    


    